#!/usr/bin/env python3
"""
Master Agent - Vision Interpreter and System Bootstrap

This is the core agent that:
1. Reads and interprets any project vision
2. Generates a constitution from vision principles
3. Creates specialized agents based on needs
4. Establishes communication protocols
5. Bootstraps the entire multi-agent system
"""

import os
import re
import yaml
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime


class MasterAgent:
    """
    Master Agent responsible for interpreting vision and bootstrapping
    the multi-agent system for any project.
    """
    
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.vision_path = None
        self.vision_data = None
        self.constitution = None
        self.agents = []
        self.protocol = None
    
    def discover_vision(self) -> Optional[Path]:
        """Discover vision document in the repository"""
        possible_locations = [
            "docs/product/vision.md",
            "docs/vision.md",
            "VISION.md",
            "README.md"  # Fallback to README
        ]
        
        for location in possible_locations:
            path = self.repo_root / location
            if path.exists():
                self.vision_path = path
                return path
        
        return None
    
    def interpret_vision(self, vision_path: str = None) -> Dict[str, Any]:
        """
        Interpret vision document to extract:
        - Mission/Purpose
        - Core principles
        - Goals (short/long term)
        - Constraints
        - Success criteria
        - Domain/industry
        """
        if vision_path:
            self.vision_path = Path(vision_path)
        elif not self.vision_path:
            self.discover_vision()
        
        if not self.vision_path or not self.vision_path.exists():
            raise FileNotFoundError("Vision document not found")
        
        with open(self.vision_path, 'r') as f:
            content = f.read()
        
        # Extract key components
        vision_data = {
            'mission': self._extract_mission(content),
            'principles': self._extract_principles(content),
            'goals': self._extract_goals(content),
            'constraints': self._extract_constraints(content),
            'success_criteria': self._extract_success_criteria(content),
            'domain': self._infer_domain(content),
            'stakeholders': self._identify_stakeholders(content),
            'values': self._extract_values(content),
            'architecture_hints': self._extract_architecture_hints(content)
        }
        
        self.vision_data = vision_data
        return vision_data
    
    def generate_constitution(self) -> Dict[str, Any]:
        """
        Generate project constitution from vision.
        Constitution defines:
        - Core laws/principles that cannot be violated
        - Decision-making framework
        - Quality gates
        - Review criteria
        - Escalation paths
        """
        if not self.vision_data:
            self.interpret_vision()
        
        constitution = {
            'version': '1.0',
            'created': datetime.now().isoformat(),
            'source_vision': str(self.vision_path),
            
            'core_laws': self._derive_core_laws(),
            'principles': self._derive_principles(),
            'decision_framework': self._create_decision_framework(),
            'quality_gates': self._define_quality_gates(),
            'review_criteria': self._define_review_criteria(),
            'enforcement': self._define_enforcement_rules(),
            'escalation': self._define_escalation_paths()
        }
        
        self.constitution = constitution
        return constitution
    
    def identify_required_agents(self) -> List[Dict[str, Any]]:
        """
        Analyze vision to determine what specialized agents are needed.
        Returns specifications for agent creation.
        """
        if not self.vision_data:
            self.interpret_vision()
        
        required_agents = []
        
        # Core coordination agents (always needed)
        required_agents.extend(self._core_coordination_agents())
        
        # Domain-specific agents based on vision analysis
        required_agents.extend(self._domain_specific_agents())
        
        # Enforcement agents based on constitution
        required_agents.extend(self._enforcement_agents())
        
        self.agents = required_agents
        return required_agents
    
    def generate_communication_protocol(self) -> Dict[str, Any]:
        """
        Generate communication protocol tailored to this project's needs.
        Includes message formats, coordination patterns, and workflows.
        """
        if not self.vision_data:
            self.interpret_vision()
        
        protocol = {
            'version': '1.0',
            'created': datetime.now().isoformat(),
            
            'message_formats': self._define_message_formats(),
            'coordination_patterns': self._define_coordination_patterns(),
            'workflows': self._define_workflows(),
            'state_management': self._define_state_management(),
            'conflict_resolution': self._define_conflict_resolution(),
            'reporting_structure': self._define_reporting_structure()
        }
        
        self.protocol = protocol
        return protocol
    
    def bootstrap_system(self, output_dir: str = None) -> Dict[str, Any]:
        """
        Complete bootstrap process:
        1. Interpret vision
        2. Generate constitution
        3. Create agents
        4. Establish protocols
        5. Initialize coordination
        """
        if not output_dir:
            output_dir = self.repo_root / ".mas-system"
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print("🎯 Master Agent: Starting system bootstrap...")
        
        # Step 1: Interpret vision
        print("\n📖 Step 1: Interpreting vision...")
        vision_data = self.interpret_vision()
        print(f"   ✓ Mission: {vision_data['mission'][:100]}...")
        print(f"   ✓ Domain: {vision_data['domain']}")
        print(f"   ✓ Principles: {len(vision_data['principles'])} identified")
        
        # Step 2: Generate constitution
        print("\n📜 Step 2: Generating constitution...")
        constitution = self.generate_constitution()
        print(f"   ✓ Core laws: {len(constitution['core_laws'])}")
        print(f"   ✓ Quality gates: {len(constitution['quality_gates'])}")
        
        # Step 3: Identify required agents
        print("\n🤖 Step 3: Identifying required agents...")
        agents = self.identify_required_agents()
        print(f"   ✓ Agents required: {len(agents)}")
        for agent in agents:
            print(f"      - {agent['title']} ({agent['type']})")
        
        # Step 4: Generate communication protocol
        print("\n💬 Step 4: Generating communication protocol...")
        protocol = self.generate_communication_protocol()
        print(f"   ✓ Message formats: {len(protocol['message_formats'])}")
        print(f"   ✓ Workflows: {len(protocol['workflows'])}")
        
        # Step 5: Save all artifacts
        print("\n💾 Step 5: Saving system artifacts...")
        artifacts = self._save_artifacts(output_dir)
        
        print("\n✅ Bootstrap complete!")
        print(f"\n📦 Artifacts saved to: {output_dir}")
        print("\n🚀 Next steps:")
        print("   1. Review generated constitution")
        print("   2. Validate agent definitions")
        print("   3. Initialize agent coordination")
        print("   4. Begin execution")
        
        return {
            'vision': vision_data,
            'constitution': constitution,
            'agents': agents,
            'protocol': protocol,
            'artifacts': artifacts
        }
    
    # ===== Private Helper Methods =====
    
    def _extract_mission(self, content: str) -> str:
        """Extract mission statement from content"""
        patterns = [
            r'#{1,3}\s+Mission.*?\n+(.*?)(?=\n#{1,3}|\Z)',
            r'#{1,3}\s+Purpose.*?\n+(.*?)(?=\n#{1,3}|\Z)',
            r'#{1,3}\s+Overview.*?\n+(.*?)(?=\n#{1,3}|\Z)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()[:500]
        
        # Fallback: first paragraph
        paragraphs = content.split('\n\n')
        return paragraphs[0].strip()[:500] if paragraphs else "Mission not specified"
    
    def _extract_principles(self, content: str) -> List[str]:
        """Extract guiding principles"""
        section_keywords = ['principle', 'value', 'philosophy', 'approach']
        principles = []
        
        for keyword in section_keywords:
            # Pattern explanation:
            # - #{1,3}\s+.*     : Match heading (H1-H3) with any text
            # - keyword         : Must contain the keyword (principle, value, etc.)
            # - [^\n]*          : Rest of heading line (excluding newline)
            # - \n+             : One or more newlines after heading
            # - ([^#].*?)       : Capture content that doesn't start with # (not another heading)
            # - (?=\n#{1,3}|\Z) : Stop at next heading or end of content
            # Note: Using r-string concatenation to avoid f-string brace issues with {1,3}
            pattern = r'#{1,3}\s+.*' + keyword + r'[^\n]*\n+([^#].*?)(?=\n#{1,3}|\Z)'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                section = match.group(1)
                principles.extend(self._extract_list_items(section))
        
        return list(set(principles))[:10]  # Top 10 unique principles
    
    def _extract_goals(self, content: str) -> Dict[str, List[str]]:
        """Extract short-term and long-term goals"""
        goals = {'short_term': [], 'long_term': []}
        
        short_pattern = r'#{1,3}\s+.*(?:short.?term|6.?month|year.?1).*?\n+(.*?)(?=\n#{1,3}|\Z)'
        long_pattern = r'#{1,3}\s+.*(?:long.?term|year.?[23]|future).*?\n+(.*?)(?=\n#{1,3}|\Z)'
        
        short_match = re.search(short_pattern, content, re.DOTALL | re.IGNORECASE)
        if short_match:
            goals['short_term'] = self._extract_list_items(short_match.group(1))
        
        long_match = re.search(long_pattern, content, re.DOTALL | re.IGNORECASE)
        if long_match:
            goals['long_term'] = self._extract_list_items(long_match.group(1))
        
        return goals
    
    def _extract_constraints(self, content: str) -> List[str]:
        """Extract constraints from vision"""
        pattern = r'#{1,3}\s+.*constraint.*?\n+(.*?)(?=\n#{1,3}|\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            return self._extract_list_items(match.group(1))
        return []
    
    def _extract_success_criteria(self, content: str) -> List[str]:
        """Extract success criteria"""
        pattern = r'#{1,3}\s+.*success.*?\n+(.*?)(?=\n#{1,3}|\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            return self._extract_list_items(match.group(1))
        return []
    
    def _infer_domain(self, content: str) -> str:
        """Infer project domain/industry from content"""
        domain_keywords = {
            'education': ['learn', 'student', 'course', 'teach', 'education'],
            'healthcare': ['health', 'medical', 'patient', 'clinical', 'hospital'],
            'finance': ['financial', 'banking', 'payment', 'transaction', 'trading'],
            'ecommerce': ['shop', 'product', 'cart', 'checkout', 'order'],
            'social': ['social', 'community', 'connect', 'share', 'network'],
            'iot': ['device', 'sensor', 'embedded', 'hardware', 'iot'],
            'enterprise': ['business', 'enterprise', 'organization', 'workflow'],
            'gaming': ['game', 'player', 'level', 'score', 'gameplay'],
            'media': ['content', 'video', 'stream', 'media', 'publish']
        }
        
        content_lower = content.lower()
        domain_scores = {}
        
        for domain, keywords in domain_keywords.items():
            score = sum(content_lower.count(kw) for kw in keywords)
            domain_scores[domain] = score
        
        top_domain = max(domain_scores.items(), key=lambda x: x[1])
        return top_domain[0] if top_domain[1] > 0 else 'general'
    
    def _identify_stakeholders(self, content: str) -> List[str]:
        """Identify key stakeholders"""
        stakeholder_patterns = [
            r'for\s+(\w+s)',  # "for teachers", "for users"
            r'(\w+)\s+can',   # "Teachers can", "Users can"
            r'target\s+(\w+)',
        ]
        
        stakeholders = set()
        for pattern in stakeholder_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            stakeholders.update(m.lower() for m in matches)
        
        return list(stakeholders)[:5]
    
    def _extract_values(self, content: str) -> List[str]:
        """Extract core values"""
        # Look for quality adjectives and value statements
        value_keywords = ['simple', 'secure', 'reliable', 'fast', 'accessible',
                         'private', 'open', 'transparent', 'scalable', 'resilient']
        
        content_lower = content.lower()
        values = [v for v in value_keywords if v in content_lower]
        
        return values[:7]
    
    def _extract_architecture_hints(self, content: str) -> List[str]:
        """Extract architectural hints from vision"""
        arch_keywords = ['architecture', 'platform', 'infrastructure', 'system',
                        'offline', 'cloud', 'mobile', 'web', 'api', 'microservice']
        
        hints = []
        content_lower = content.lower()
        
        for keyword in arch_keywords:
            if keyword in content_lower:
                # Extract sentence containing keyword
                sentences = re.split(r'[.!?]', content)
                for sentence in sentences:
                    if keyword in sentence.lower():
                        hints.append(sentence.strip())
                        break
        
        return hints[:5]
    
    def _extract_list_items(self, content: str) -> List[str]:
        """Extract bullet/numbered list items"""
        items = []
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith(('-', '*', '•')) or re.match(r'^\d+\.', line):
                item = re.sub(r'^[-*•]\s*|\d+\.\s*', '', line)
                if item and len(item) > 5:
                    items.append(item)
        return items
    
    def _derive_core_laws(self) -> List[Dict[str, str]]:
        """Derive inviolable core laws from principles"""
        principles = self.vision_data.get('principles', [])
        values = self.vision_data.get('values', [])
        
        core_laws = []
        
        # Convert top principles to core laws
        for i, principle in enumerate(principles[:5]):
            core_laws.append({
                'id': f'LAW-{i+1:03d}',
                'principle': principle,
                'enforcement': 'automatic',
                'violation_action': 'reject'
            })
        
        return core_laws
    
    def _derive_principles(self) -> List[Dict[str, str]]:
        """Derive working principles from vision"""
        return [
            {
                'id': 'PRIN-001',
                'name': 'Vision Alignment',
                'description': 'All work must align with project vision',
                'validation': 'Check against vision goals'
            },
            {
                'id': 'PRIN-002',
                'name': 'Quality First',
                'description': 'Quality cannot be compromised for speed',
                'validation': 'All quality gates must pass'
            },
            {
                'id': 'PRIN-003',
                'name': 'Simplicity',
                'description': 'Choose simple solutions over complex',
                'validation': 'Complexity review required'
            }
        ]
    
    def _create_decision_framework(self) -> Dict[str, Any]:
        """Create decision-making framework"""
        return {
            'agent_authority': {
                'implement': 'Implementation details',
                'propose': 'Architectural changes',
                'escalate': 'Vision/principle changes'
            },
            'review_required': [
                'Breaking changes',
                'New dependencies',
                'Architecture decisions',
                'Security changes'
            ],
            'approval_levels': {
                'code': 'any-agent',
                'architecture': 'enforcement-agent',
                'vision': 'human'
            }
        }
    
    def _define_quality_gates(self) -> List[Dict[str, Any]]:
        """Define quality gates"""
        gates = [
            {
                'name': 'Code Quality',
                'checks': ['linting', 'tests', 'coverage'],
                'required': True
            },
            {
                'name': 'Vision Alignment',
                'checks': ['goals', 'principles', 'constraints'],
                'required': True
            },
            {
                'name': 'Security',
                'checks': ['vulnerability-scan', 'secrets-check'],
                'required': True
            }
        ]
        
        # Add domain-specific gates
        domain = self.vision_data.get('domain')
        if domain == 'education':
            gates.append({
                'name': 'Accessibility',
                'checks': ['wcag', 'screen-reader'],
                'required': True
            })
        
        return gates
    
    def _define_review_criteria(self) -> List[str]:
        """Define review criteria"""
        return [
            'Aligns with vision',
            'Follows principles',
            'Meets quality gates',
            'Has adequate tests',
            'Documentation updated',
            'No security issues'
        ]
    
    def _define_enforcement_rules(self) -> Dict[str, Any]:
        """Define how constitution is enforced"""
        return {
            'automatic': [
                'Linting',
                'Tests',
                'Security scans'
            ],
            'agent_review': [
                'Code review',
                'Architecture review',
                'Complexity review'
            ],
            'human_approval': [
                'Vision changes',
                'Release decisions',
                'Major pivots'
            ]
        }
    
    def _define_escalation_paths(self) -> Dict[str, Any]:
        """Define escalation paths for issues"""
        return {
            'technical_blocker': 'coordination-agent',
            'architecture_conflict': 'enforcement-agent',
            'vision_conflict': 'human',
            'resource_constraint': 'human'
        }
    
    def _core_coordination_agents(self) -> List[Dict[str, Any]]:
        """Define core coordination agents (always needed)"""
        return [
            {
                'agent_id': 'master-coordinator',
                'title': 'Master Coordination Agent',
                'type': 'coordination',
                'role': 'Orchestrate overall system execution',
                'authority': 'coordinate',
                'responsibilities': [
                    'Sprint planning',
                    'Task assignment',
                    'Progress tracking',
                    'Blocker resolution'
                ]
            },
            {
                'agent_id': 'task-dispatcher',
                'title': 'Task Dispatcher Agent',
                'type': 'coordination',
                'role': 'Assign tasks to appropriate agents',
                'authority': 'assign',
                'responsibilities': [
                    'Task analysis',
                    'Agent matching',
                    'Load balancing',
                    'Priority management'
                ]
            }
        ]
    
    def _domain_specific_agents(self) -> List[Dict[str, Any]]:
        """Identify domain-specific agents based on vision analysis"""
        domain = self.vision_data.get('domain')
        agents = []
        
        # Common agents for any domain
        agents.extend([
            {
                'agent_id': 'implementation-agent',
                'title': 'Implementation Agent',
                'type': 'development',
                'role': 'Implement features and functionality',
                'authority': 'implement'
            },
            {
                'agent_id': 'test-agent',
                'title': 'Quality Assurance Agent',
                'type': 'development',
                'role': 'Ensure quality through testing',
                'authority': 'validate'
            },
            {
                'agent_id': 'documentation-agent',
                'title': 'Documentation Agent',
                'type': 'development',
                'role': 'Maintain project documentation',
                'authority': 'document'
            }
        ])
        
        # Domain-specific specializations
        if 'mobile' in str(self.vision_data.get('architecture_hints', [])).lower():
            agents.append({
                'agent_id': 'mobile-agent',
                'title': 'Mobile Development Agent',
                'type': 'development',
                'role': 'Develop mobile applications',
                'authority': 'implement'
            })
        
        if 'api' in str(self.vision_data.get('architecture_hints', [])).lower():
            agents.append({
                'agent_id': 'api-agent',
                'title': 'API Development Agent',
                'type': 'development',
                'role': 'Design and implement APIs',
                'authority': 'implement'
            })
        
        return agents
    
    def _enforcement_agents(self) -> List[Dict[str, Any]]:
        """Define enforcement agents based on constitution"""
        return [
            {
                'agent_id': 'constitutional-judge',
                'title': 'Constitutional Judge Agent',
                'type': 'enforcement',
                'role': 'Ensure compliance with constitution',
                'authority': 'enforce',
                'responsibilities': [
                    'Review changes for principle violations',
                    'Validate vision alignment',
                    'Enforce core laws'
                ]
            },
            {
                'agent_id': 'security-enforcer',
                'title': 'Security Enforcement Agent',
                'type': 'enforcement',
                'role': 'Ensure security standards',
                'authority': 'enforce',
                'responsibilities': [
                    'Security scanning',
                    'Vulnerability detection',
                    'Secret detection'
                ]
            },
            {
                'agent_id': 'quality-enforcer',
                'title': 'Quality Enforcement Agent',
                'type': 'enforcement',
                'role': 'Ensure quality standards',
                'authority': 'enforce',
                'responsibilities': [
                    'Code quality checks',
                    'Test coverage validation',
                    'Performance validation'
                ]
            }
        ]
    
    def _define_message_formats(self) -> Dict[str, Any]:
        """Define standard message formats"""
        return {
            'status_update': {
                'agent': 'string',
                'task': 'string',
                'status': ['in-progress', 'completed', 'blocked', 'failed'],
                'progress': 'object',
                'context': 'array'
            },
            'task_request': {
                'from_agent': 'string',
                'to_agent': 'string',
                'task': 'string',
                'priority': ['high', 'medium', 'low'],
                'deadline': 'datetime'
            },
            'decision_request': {
                'agent': 'string',
                'decision': 'string',
                'options': 'array',
                'recommendation': 'string',
                'rationale': 'string'
            }
        }
    
    def _define_coordination_patterns(self) -> Dict[str, Any]:
        """Define coordination patterns"""
        return {
            'parallel': 'Independent tasks executed simultaneously',
            'sequential': 'Tasks with dependencies executed in order',
            'divide_conquer': 'Large task split among multiple agents',
            'review_iterate': 'Cycles of implementation and review'
        }
    
    def _define_workflows(self) -> Dict[str, List[str]]:
        """Define standard workflows"""
        return {
            'feature_development': [
                'Design',
                'Implementation',
                'Testing',
                'Review',
                'Documentation',
                'Deployment'
            ],
            'bug_fix': [
                'Investigation',
                'Fix Implementation',
                'Testing',
                'Review',
                'Deployment'
            ],
            'architecture_decision': [
                'Problem Analysis',
                'Options Exploration',
                'Decision Proposal',
                'Review',
                'ADR Creation',
                'Implementation'
            ]
        }
    
    def _define_state_management(self) -> Dict[str, str]:
        """Define how shared state is managed"""
        return {
            'sprint_plan': 'YAML file in tools/agent-orchestration/',
            'task_status': 'GitHub Issues',
            'code_changes': 'Pull Requests',
            'decisions': 'ADRs in docs/adr/',
            'agent_coordination': 'Coordination issues'
        }
    
    def _define_conflict_resolution(self) -> Dict[str, str]:
        """Define conflict resolution strategies"""
        return {
            'design_conflict': 'Consult constitution and vision',
            'priority_conflict': 'Sprint goal alignment',
            'resource_conflict': 'Critical path priority',
            'technical_conflict': 'Enforcement agent decision',
            'vision_conflict': 'Human escalation'
        }
    
    def _define_reporting_structure(self) -> Dict[str, Any]:
        """Define reporting structure"""
        return {
            'frequency': {
                'status_updates': 'daily',
                'progress_reports': 'weekly',
                'sprint_reviews': 'end_of_sprint'
            },
            'channels': {
                'status': 'GitHub Issues',
                'progress': 'PR descriptions',
                'reviews': 'Discussion threads'
            }
        }
    
    def _save_artifacts(self, output_dir: Path) -> Dict[str, str]:
        """Save all generated artifacts"""
        artifacts = {}
        
        # Save vision analysis
        vision_file = output_dir / "vision-analysis.yaml"
        with open(vision_file, 'w') as f:
            yaml.dump(self.vision_data, f, default_flow_style=False)
        artifacts['vision_analysis'] = str(vision_file)
        
        # Save constitution
        constitution_file = output_dir / "constitution.yaml"
        with open(constitution_file, 'w') as f:
            yaml.dump(self.constitution, f, default_flow_style=False)
        artifacts['constitution'] = str(constitution_file)
        
        # Save agent specifications
        agents_file = output_dir / "agent-specifications.yaml"
        with open(agents_file, 'w') as f:
            yaml.dump({'agents': self.agents}, f, default_flow_style=False)
        artifacts['agents'] = str(agents_file)
        
        # Save communication protocol
        protocol_file = output_dir / "communication-protocol.yaml"
        with open(protocol_file, 'w') as f:
            yaml.dump(self.protocol, f, default_flow_style=False)
        artifacts['protocol'] = str(protocol_file)
        
        # Save bootstrap summary
        summary_file = output_dir / "bootstrap-summary.md"
        with open(summary_file, 'w') as f:
            f.write(self._generate_summary())
        artifacts['summary'] = str(summary_file)
        
        return artifacts
    
    def _generate_summary(self) -> str:
        """Generate markdown summary of bootstrap"""
        return f"""# Multi-Agent System Bootstrap Summary

## Vision Analysis

**Domain**: {self.vision_data.get('domain', 'N/A')}
**Mission**: {self.vision_data.get('mission', 'N/A')[:200]}...

### Core Principles ({len(self.vision_data.get('principles', []))})
{chr(10).join(f'- {p}' for p in self.vision_data.get('principles', [])[:5])}

### Success Criteria ({len(self.vision_data.get('success_criteria', []))})
{chr(10).join(f'- {c}' for c in self.vision_data.get('success_criteria', [])[:5])}

## Constitution

**Core Laws**: {len(self.constitution.get('core_laws', []))}
**Quality Gates**: {len(self.constitution.get('quality_gates', []))}

## Agent System

**Total Agents**: {len(self.agents)}

### By Type
- Coordination: {len([a for a in self.agents if a.get('type') == 'coordination'])}
- Development: {len([a for a in self.agents if a.get('type') == 'development'])}
- Enforcement: {len([a for a in self.agents if a.get('type') == 'enforcement'])}

### Agent List
{chr(10).join(f'- {a.get("title")} ({a.get("agent_id")})' for a in self.agents)}

## Communication Protocol

**Message Formats**: {len(self.protocol.get('message_formats', {}))}
**Coordination Patterns**: {len(self.protocol.get('coordination_patterns', {}))}
**Workflows**: {len(self.protocol.get('workflows', {}))}

## Next Steps

1. Review generated constitution for accuracy
2. Validate agent specifications
3. Create agent definition files
4. Initialize coordination system
5. Begin sprint planning and execution

---
Generated by Master Agent on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Master Agent - Bootstrap Multi-Agent System')
    parser.add_argument('--repo-root', default=None, help='Repository root path')
    parser.add_argument('--vision', default=None, help='Path to vision document')
    parser.add_argument('--output', default=None, help='Output directory for artifacts')
    parser.add_argument('--action', choices=['interpret', 'constitution', 'agents', 'protocol', 'bootstrap'],
                       default='bootstrap', help='Action to perform')
    
    args = parser.parse_args()
    
    master = MasterAgent(args.repo_root)
    
    try:
        if args.action == 'interpret':
            vision = master.interpret_vision(args.vision)
            print(yaml.dump(vision, default_flow_style=False))
        
        elif args.action == 'constitution':
            master.interpret_vision(args.vision)
            constitution = master.generate_constitution()
            print(yaml.dump(constitution, default_flow_style=False))
        
        elif args.action == 'agents':
            master.interpret_vision(args.vision)
            agents = master.identify_required_agents()
            print(yaml.dump({'agents': agents}, default_flow_style=False))
        
        elif args.action == 'protocol':
            master.interpret_vision(args.vision)
            protocol = master.generate_communication_protocol()
            print(yaml.dump(protocol, default_flow_style=False))
        
        elif args.action == 'bootstrap':
            result = master.bootstrap_system(args.output)
            print(f"\n✅ System bootstrapped successfully!")
            print(f"📂 Artifacts: {result['artifacts']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
