#!/usr/bin/env python3
"""
Agent Self-Creation System

Allows agents to propose and create new specialized agent definitions
based on identified needs during execution.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime


class AgentCreator:
    """System for creating new agent definitions"""
    
    AGENT_TEMPLATE = """# {title}

## Role
{role_description}

## Authority
**{authority_level}** - {authority_description}

## Responsibilities

{responsibilities}

## Required Capabilities

{capabilities}

## Communication Protocol

### Status Reports
```yaml
agent: {agent_id}
task: [task-description]
status: [in-progress|completed|blocked|failed]
progress:
  - completed: [list of completed items]
  - in-progress: [current work]
  - blocked: [blockers if any]
context:
  - [relevant context, decisions, tradeoffs]
```

### Task Requests
```yaml
request_from: {agent_id}
task_type: {task_type}
priority: [high|medium|low]
description: [detailed description]
acceptance_criteria:
  - [criterion 1]
  - [criterion 2]
```

## Integration Points

### With Other Agents
{integration_points}

### With Workflows
- Triggered by: {triggers}
- Reports to: {reports_to}
- Coordinates with: {coordinates_with}

## Quality Gates

{quality_gates}

## Success Criteria

{success_criteria}

## Related Documents

- [Communication Protocol](../communication-protocol.md)
- [PR Merge Constitution](../pr-merge-constitution.yaml)
{related_docs}

## Notes

{notes}

---

*Agent created: {created_date}*
*Created by: {creator}*
*Purpose: {purpose}*
"""

    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.agents_dir = self.repo_root / ".github" / "agents"
        self.mutagen_dir = self.agents_dir / "mutagen-agents"
        self.enforcement_dir = self.agents_dir / "enforcement-agents"
    
    def analyze_task_patterns(self, sprint_plan_path: str = None) -> Dict[str, Any]:
        """Analyze sprint tasks to identify needed agent specializations"""
        if not sprint_plan_path:
            sprint_plan_path = self.repo_root / "tools" / "agent-orchestration" / "current-sprint.yaml"
        
        with open(sprint_plan_path, 'r') as f:
            sprint_plan = yaml.safe_load(f)
        
        # Count tasks by agent type
        agent_needs = {}
        for task in sprint_plan.get('tasks', []):
            agent_type = task.get('agent_type', 'general-agent')
            if agent_type not in agent_needs:
                agent_needs[agent_type] = {
                    'count': 0,
                    'tasks': [],
                    'complexity': []
                }
            agent_needs[agent_type]['count'] += 1
            agent_needs[agent_type]['tasks'].append(task['description'])
            agent_needs[agent_type]['complexity'].append(task.get('estimated_points', 2))
        
        # Identify high-demand specializations
        suggestions = []
        for agent_type, data in agent_needs.items():
            if data['count'] >= 3:  # Threshold for creating specialized agent
                avg_complexity = sum(data['complexity']) / len(data['complexity'])
                suggestions.append({
                    'agent_type': agent_type,
                    'task_count': data['count'],
                    'avg_complexity': avg_complexity,
                    'sample_tasks': data['tasks'][:3],
                    'priority': 'high' if data['count'] >= 5 else 'medium'
                })
        
        return {
            'suggestions': sorted(suggestions, key=lambda x: x['task_count'], reverse=True),
            'total_tasks': len(sprint_plan.get('tasks', [])),
            'unique_agent_types': len(agent_needs)
        }
    
    def propose_agent(self, agent_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Propose a new agent definition"""
        proposal = {
            'agent_id': agent_spec['agent_id'],
            'title': agent_spec['title'],
            'role': agent_spec.get('role', 'Specialized agent for specific tasks'),
            'type': agent_spec.get('type', 'mutagen'),  # mutagen or enforcement
            'rationale': agent_spec.get('rationale', 'High task volume requires specialization'),
            'capabilities': agent_spec.get('capabilities', []),
            'status': 'proposed',
            'proposed_date': datetime.now().isoformat(),
            'proposed_by': agent_spec.get('proposed_by', 'system')
        }
        
        return proposal
    
    def create_agent_file(self, agent_spec: Dict[str, Any]) -> str:
        """Create agent definition file from specification"""
        agent_type = agent_spec.get('type', 'mutagen')
        target_dir = self.mutagen_dir if agent_type == 'mutagen' else self.enforcement_dir
        
        # Generate file content from template
        content = self.AGENT_TEMPLATE.format(
            title=agent_spec['title'],
            agent_id=agent_spec['agent_id'],
            role_description=agent_spec.get('role', 'Specialized development agent'),
            authority_level=agent_spec.get('authority_level', 'Execute'),
            authority_description=agent_spec.get('authority_description', 
                'Can implement features and make implementation decisions within scope'),
            responsibilities=self._format_list(agent_spec.get('responsibilities', [
                'Implement assigned tasks',
                'Follow coding standards',
                'Write tests',
                'Document changes'
            ])),
            capabilities=self._format_list(agent_spec.get('capabilities', [
                'Code implementation',
                'Testing',
                'Documentation'
            ])),
            task_type=agent_spec.get('task_type', 'implementation'),
            triggers=agent_spec.get('triggers', 'Task assignment'),
            reports_to=agent_spec.get('reports_to', 'Sprint Driver Agent'),
            coordinates_with=agent_spec.get('coordinates_with', 'Other development agents'),
            integration_points=agent_spec.get('integration_points', 
                '- Collaborates with other agents on complex features\n- Reports progress to coordination system'),
            quality_gates=agent_spec.get('quality_gates', 
                '- Code review passed\n- Tests passing\n- Documentation updated'),
            success_criteria=agent_spec.get('success_criteria',
                '- Tasks completed on time\n- Quality standards met\n- No blocking issues'),
            related_docs=agent_spec.get('related_docs', ''),
            notes=agent_spec.get('notes', 'This agent was created automatically based on task analysis.'),
            created_date=datetime.now().strftime('%Y-%m-%d'),
            creator=agent_spec.get('proposed_by', 'Autonomous Agent System'),
            purpose=agent_spec.get('rationale', 'Identified need for specialization')
        )
        
        # Save to file
        filename = f"{agent_spec['agent_id']}.md"
        filepath = target_dir / filename
        
        target_dir.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        
        return str(filepath)
    
    def _format_list(self, items: List[str]) -> str:
        """Format a list of items as markdown"""
        if not items:
            return '- (To be defined)'
        return '\n'.join(f"- {item}" for item in items)
    
    def suggest_agents_from_sprint(self, sprint_plan_path: str = None) -> List[Dict[str, Any]]:
        """Analyze sprint and suggest agent creations"""
        analysis = self.analyze_task_patterns(sprint_plan_path)
        suggestions = []
        
        for suggestion in analysis['suggestions']:
            agent_type = suggestion['agent_type']
            
            # Map generic types to specific agent specs
            agent_specs = self._generate_agent_spec(agent_type, suggestion)
            if agent_specs:
                suggestions.append(agent_specs)
        
        return suggestions
    
    def _generate_agent_spec(self, agent_type: str, analysis: Dict) -> Dict[str, Any]:
        """Generate detailed agent specification from analysis"""
        specs = {
            'ui-agent': {
                'agent_id': 'ui-development-agent',
                'title': 'UI Development Agent',
                'role': 'Develop user interface components and screens for the mobile app',
                'authority_level': 'Implement',
                'authority_description': 'Can implement UI components, make styling decisions, and ensure mobile-first design',
                'responsibilities': [
                    'Implement mobile UI components',
                    'Ensure offline-first UI patterns',
                    'Optimize for low-end devices',
                    'Follow mobile design guidelines',
                    'Write UI tests'
                ],
                'capabilities': [
                    'React Native/Flutter development',
                    'Mobile UI/UX implementation',
                    'Responsive design',
                    'Accessibility compliance',
                    'Performance optimization'
                ],
                'task_type': 'ui-implementation',
                'quality_gates': '- UI renders correctly on 2GB device\n- Works in airplane mode\n- Passes accessibility checks\n- Performance targets met'
            },
            'data-agent': {
                'agent_id': 'data-layer-agent',
                'title': 'Data Layer Agent',
                'role': 'Design and implement data storage, models, and offline sync',
                'authority_level': 'Implement',
                'authority_description': 'Can design data schemas, implement storage, and create sync logic',
                'responsibilities': [
                    'Design data models',
                    'Implement local storage (SQLite)',
                    'Create sync mechanisms',
                    'Handle data migrations',
                    'Ensure data integrity'
                ],
                'capabilities': [
                    'Database design',
                    'SQLite/local storage',
                    'Sync logic implementation',
                    'Data validation',
                    'Migration strategies'
                ],
                'task_type': 'data-implementation',
                'quality_gates': '- Schema is optimized\n- Data persists correctly\n- Sync handles conflicts\n- No data loss scenarios'
            },
            'test-agent': {
                'agent_id': 'quality-assurance-agent',
                'title': 'Quality Assurance Agent',
                'role': 'Implement comprehensive testing for features',
                'authority_level': 'Validate',
                'authority_description': 'Can create tests, validate quality, and enforce testing standards',
                'responsibilities': [
                    'Write unit tests',
                    'Create integration tests',
                    'Test offline scenarios',
                    'Performance testing',
                    'Device compatibility testing'
                ],
                'capabilities': [
                    'Test framework expertise',
                    'Offline testing',
                    'Device simulation',
                    'Performance profiling',
                    'Test automation'
                ],
                'task_type': 'testing',
                'quality_gates': '- 80%+ code coverage\n- All offline scenarios tested\n- Device tests passing\n- Performance validated'
            },
            'doc-agent': {
                'agent_id': 'documentation-agent',
                'title': 'Documentation Agent',
                'role': 'Create and maintain project documentation',
                'authority_level': 'Document',
                'authority_description': 'Can write documentation, maintain guides, and ensure clarity',
                'responsibilities': [
                    'Write user documentation',
                    'Maintain developer guides',
                    'Create API documentation',
                    'Update ADRs as needed',
                    'Ensure documentation accuracy'
                ],
                'capabilities': [
                    'Technical writing',
                    'Documentation tools',
                    'API documentation',
                    'Tutorial creation',
                    'Markdown expertise'
                ],
                'task_type': 'documentation',
                'quality_gates': '- Documentation is clear\n- Examples work\n- Links are valid\n- Stays synchronized with code'
            },
            'backend-agent': {
                'agent_id': 'backend-development-agent',
                'title': 'Backend Development Agent',
                'role': 'Implement backend services and APIs (optional features)',
                'authority_level': 'Implement',
                'authority_description': 'Can implement APIs and services with offline-first principle',
                'responsibilities': [
                    'Design REST/GraphQL APIs',
                    'Implement sync endpoints',
                    'Ensure APIs are optional',
                    'Handle authentication',
                    'Optimize for low bandwidth'
                ],
                'capabilities': [
                    'API design',
                    'Backend development',
                    'Database integration',
                    'Security implementation',
                    'Performance optimization'
                ],
                'task_type': 'backend-implementation',
                'quality_gates': '- API is optional (offline works)\n- Secure authentication\n- Handles low bandwidth\n- Proper error handling'
            }
        }
        
        spec = specs.get(agent_type)
        if spec:
            spec['rationale'] = f"High volume of {agent_type} tasks ({analysis['task_count']} tasks) requires dedicated specialization"
            spec['sample_tasks'] = analysis['sample_tasks']
            spec['priority'] = analysis['priority']
            spec['type'] = 'mutagen'
            spec['proposed_by'] = 'Agent Coordination System'
        
        return spec


def main():
    """CLI entry point"""
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description='Agent self-creation system')
    parser.add_argument('--repo-root', default=None, help='Repository root path')
    parser.add_argument('--action', choices=['analyze', 'suggest', 'create'], 
                       default='suggest', help='Action to perform')
    parser.add_argument('--sprint-plan', default=None, help='Sprint plan YAML file')
    parser.add_argument('--agent-spec', default=None, help='Agent specification JSON file')
    
    args = parser.parse_args()
    
    creator = AgentCreator(args.repo_root)
    
    try:
        if args.action == 'analyze':
            analysis = creator.analyze_task_patterns(args.sprint_plan)
            print("📊 Task Analysis:")
            print(f"  Total tasks: {analysis['total_tasks']}")
            print(f"  Unique agent types: {analysis['unique_agent_types']}")
            print(f"  Specialization suggestions: {len(analysis['suggestions'])}")
            
        elif args.action == 'suggest':
            suggestions = creator.suggest_agents_from_sprint(args.sprint_plan)
            print(f"🤖 Agent Creation Suggestions: {len(suggestions)}")
            for spec in suggestions:
                print(f"\n  - {spec['title']} ({spec['agent_id']})")
                print(f"    Rationale: {spec['rationale']}")
                print(f"    Priority: {spec['priority']}")
            
        elif args.action == 'create':
            if not args.agent_spec:
                print("❌ Error: --agent-spec required for create action")
                return 1
            
            with open(args.agent_spec, 'r') as f:
                spec = json.load(f)
            
            filepath = creator.create_agent_file(spec)
            print(f"✅ Agent created: {filepath}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
