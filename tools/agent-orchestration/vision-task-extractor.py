#!/usr/bin/env python3
"""
Vision-based Task Extractor

Parses the project vision and backlog to extract actionable tasks
and generate sprint plans for autonomous agent execution.
"""

import os
import re
import yaml
from pathlib import Path
from typing import List, Dict, Any


class VisionTaskExtractor:
    """Extract tasks from vision and backlog documents"""
    
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.vision_path = self.repo_root / "docs" / "product" / "vision.md"
        self.backlog_path = self.repo_root / "docs" / "development" / "backlog-v1.md"
    
    def parse_vision(self) -> Dict[str, Any]:
        """Parse vision document to extract goals and priorities"""
        if not self.vision_path.exists():
            raise FileNotFoundError(f"Vision file not found: {self.vision_path}")
        
        with open(self.vision_path, 'r') as f:
            content = f.read()
        
        vision_data = {
            'mission': self._extract_section(content, 'Mission Statement'),
            'short_term_goals': self._extract_list_items(
                self._extract_section(content, 'Short Term')
            ),
            'guiding_principles': self._extract_list_items(
                self._extract_section(content, 'Guiding Principles')
            ),
            'success_criteria': self._extract_list_items(
                self._extract_section(content, 'Success Criteria')
            )
        }
        
        return vision_data
    
    def parse_backlog(self) -> Dict[str, List[Dict[str, Any]]]:
        """Parse backlog to extract epics and stories"""
        if not self.backlog_path.exists():
            raise FileNotFoundError(f"Backlog file not found: {self.backlog_path}")
        
        with open(self.backlog_path, 'r') as f:
            content = f.read()
        
        epics = []
        epic_pattern = r'## (Epic \d+): ([^\n]+)\n\n### Priority: (\w+)\n\*\*Goal\*\*: ([^\n]+)'
        
        for match in re.finditer(epic_pattern, content):
            epic_id = match.group(1)
            epic_title = match.group(2)
            priority = match.group(3)
            goal = match.group(4)
            
            # Extract stories for this epic
            epic_section = self._extract_section(content, f'{epic_id}: {epic_title}')
            stories = self._extract_stories(epic_section)
            
            epics.append({
                'id': epic_id,
                'title': epic_title,
                'priority': priority,
                'goal': goal,
                'stories': stories
            })
        
        return {'epics': epics}
    
    def generate_sprint_plan(self, sprint_duration_days: int = 14) -> Dict[str, Any]:
        """Generate a sprint plan based on vision and backlog"""
        vision = self.parse_vision()
        backlog = self.parse_backlog()
        
        # Focus on critical priority epics aligned with short-term goals
        critical_epics = [
            epic for epic in backlog['epics']
            if epic['priority'].lower() == 'critical'
        ]
        
        sprint_plan = {
            'sprint_goal': self._determine_sprint_goal(vision, critical_epics),
            'duration_days': sprint_duration_days,
            'epics': critical_epics[:3],  # Top 3 critical epics
            'alignment': {
                'vision_goals': vision['short_term_goals'][:2],
                'success_criteria': vision['success_criteria']
            },
            'tasks': self._extract_actionable_tasks(critical_epics[:3])
        }
        
        return sprint_plan
    
    def _extract_section(self, content: str, heading: str) -> str:
        """Extract content under a specific heading"""
        pattern = rf'#{1,3}\s+{re.escape(heading)}.*?\n(.*?)(?=\n#{1,3}\s+|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else ''
    
    def _extract_list_items(self, content: str) -> List[str]:
        """Extract bullet points or numbered list items"""
        items = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith(('-', '*', '•')) or re.match(r'^\d+\.', line):
                # Remove list markers
                item = re.sub(r'^[-*•]\s*|\d+\.\s*', '', line)
                if item:
                    items.append(item)
        return items
    
    def _extract_stories(self, epic_content: str) -> List[Dict[str, Any]]:
        """Extract stories from epic section"""
        stories = []
        story_pattern = r'\*\*(\d+\.\d+)\s+([^\*]+)\*\*'
        
        for match in re.finditer(story_pattern, epic_content):
            story_id = match.group(1)
            story_title = match.group(2).strip()
            
            # Find tasks for this story (checkbox items after the story)
            story_pos = match.end()
            next_story = re.search(r'\*\*\d+\.\d+', epic_content[story_pos:])
            end_pos = story_pos + next_story.start() if next_story else len(epic_content)
            story_section = epic_content[story_pos:end_pos]
            
            tasks = self._extract_checkbox_items(story_section)
            
            stories.append({
                'id': story_id,
                'title': story_title,
                'tasks': tasks,
                'status': 'pending'
            })
        
        return stories
    
    def _extract_checkbox_items(self, content: str) -> List[str]:
        """Extract checkbox items from content"""
        items = []
        for line in content.split('\n'):
            if re.match(r'^\s*-\s*\[[ x]\]', line):
                item = re.sub(r'^\s*-\s*\[[ x]\]\s*', '', line).strip()
                if item:
                    items.append(item)
        return items
    
    def _determine_sprint_goal(self, vision: Dict, epics: List[Dict]) -> str:
        """Determine sprint goal based on vision and selected epics"""
        if not epics:
            return "Initialize project foundation"
        
        # Combine the goals of selected epics
        epic_goals = [epic['goal'] for epic in epics[:2]]
        return f"Deliver {' and '.join(epic_goals)}"
    
    def _extract_actionable_tasks(self, epics: List[Dict]) -> List[Dict[str, Any]]:
        """Convert stories into actionable tasks with metadata"""
        tasks = []
        task_id = 1
        
        for epic in epics:
            for story in epic.get('stories', []):
                for task_desc in story.get('tasks', []):
                    tasks.append({
                        'id': f'TASK-{task_id:03d}',
                        'epic': epic['title'],
                        'story': story['title'],
                        'description': task_desc,
                        'priority': epic['priority'],
                        'status': 'todo',
                        'estimated_points': self._estimate_task_points(task_desc),
                        'agent_type': self._suggest_agent_type(task_desc)
                    })
                    task_id += 1
        
        return tasks
    
    def _estimate_task_points(self, task_desc: str) -> int:
        """Simple heuristic to estimate story points"""
        keywords_complex = ['implementation', 'integration', 'system', 'architecture']
        keywords_medium = ['design', 'create', 'build', 'add']
        keywords_simple = ['setup', 'update', 'fix', 'document']
        
        task_lower = task_desc.lower()
        
        if any(kw in task_lower for kw in keywords_complex):
            return 5
        elif any(kw in task_lower for kw in keywords_medium):
            return 3
        elif any(kw in task_lower for kw in keywords_simple):
            return 1
        else:
            return 2
    
    def _suggest_agent_type(self, task_desc: str) -> str:
        """Suggest appropriate agent type for task"""
        task_lower = task_desc.lower()
        
        if any(kw in task_lower for kw in ['ui', 'screen', 'component', 'view']):
            return 'ui-agent'
        elif any(kw in task_lower for kw in ['database', 'storage', 'data', 'schema']):
            return 'data-agent'
        elif any(kw in task_lower for kw in ['test', 'testing', 'validation']):
            return 'test-agent'
        elif any(kw in task_lower for kw in ['document', 'docs', 'guide']):
            return 'doc-agent'
        elif any(kw in task_lower for kw in ['api', 'endpoint', 'service']):
            return 'backend-agent'
        else:
            return 'general-agent'
    
    def save_sprint_plan(self, output_path: str = None) -> str:
        """Generate and save sprint plan to YAML file"""
        sprint_plan = self.generate_sprint_plan()
        
        if not output_path:
            output_path = self.repo_root / "tools" / "agent-orchestration" / "current-sprint.yaml"
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            yaml.dump(sprint_plan, f, default_flow_style=False, sort_keys=False)
        
        return str(output_path)


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract tasks from vision and backlog')
    parser.add_argument('--repo-root', default=None, help='Repository root path')
    parser.add_argument('--output', default=None, help='Output file path')
    parser.add_argument('--format', choices=['yaml', 'json'], default='yaml', help='Output format')
    
    args = parser.parse_args()
    
    extractor = VisionTaskExtractor(args.repo_root)
    
    try:
        sprint_plan_path = extractor.save_sprint_plan(args.output)
        print(f"✅ Sprint plan generated: {sprint_plan_path}")
        
        # Also print summary
        sprint_plan = extractor.generate_sprint_plan()
        print(f"\n📋 Sprint Goal: {sprint_plan['sprint_goal']}")
        print(f"📅 Duration: {sprint_plan['duration_days']} days")
        print(f"📦 Epics: {len(sprint_plan['epics'])}")
        print(f"✅ Tasks: {len(sprint_plan['tasks'])}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
