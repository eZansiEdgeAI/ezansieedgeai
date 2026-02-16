#!/usr/bin/env python3
"""
Agent Definition Generator

Reads agent specifications and generates markdown definition files
in the appropriate directories (.github/agents/).
"""

import yaml
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List


class AgentDefinitionGenerator:
    """Generate agent definition files from specifications"""
    
    AGENT_TEMPLATE = """# {title}

## Role
{role}

## Authority
**{authority}** - {authority_description}

## Responsibilities

{responsibilities}

## Capabilities

{capabilities}

## Communication

### Status Updates
```yaml
agent: {agent_id}
task: [task-description]
status: [in-progress|completed|blocked|failed]
progress:
  completed: [list]
  in_progress: [list]
  blocked: [list]
context:
  - [relevant information]
```

### Task Requests
```yaml
from: {agent_id}
to: [target-agent]
task: [description]
priority: [high|medium|low]
deadline: [datetime]
```

## Integration Points

{integration}

## Quality Standards

{quality_standards}

## Success Metrics

{success_metrics}

## Related Documents

- [Communication Protocol](../communication-protocol.md)
{related_docs}

## Notes

{notes}

---

*Generated: {generated_date}*
*From: {source}*
"""

    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.agents_dir = self.repo_root / ".github" / "agents"
        self.mutagen_dir = self.agents_dir / "mutagen-agents"
        self.enforcement_dir = self.agents_dir / "enforcement-agents"
    
    def load_specifications(self, spec_file: str = None) -> List[Dict[str, Any]]:
        """Load agent specifications from YAML file"""
        if not spec_file:
            spec_file = self.repo_root / ".mas-system" / "agent-specifications.yaml"
        
        spec_file = Path(spec_file)
        if not spec_file.exists():
            raise FileNotFoundError(f"Specification file not found: {spec_file}")
        
        with open(spec_file, 'r') as f:
            data = yaml.safe_load(f)
        
        return data.get('agents', [])
    
    def generate_definition(self, agent_spec: Dict[str, Any]) -> str:
        """Generate markdown definition from specification"""
        
        # Determine authority description
        authority_map = {
            'coordinate': 'Can orchestrate work across agents, assign tasks, and make coordination decisions',
            'assign': 'Can assign tasks to agents and manage work distribution',
            'implement': 'Can implement features and make implementation decisions within scope',
            'validate': 'Can validate quality and approve/reject work',
            'document': 'Can create and update documentation',
            'enforce': 'Can enforce rules and block work that violates standards',
        }
        
        authority = agent_spec.get('authority', 'execute')
        authority_desc = authority_map.get(authority, 'Can execute assigned tasks')
        
        # Format responsibilities
        responsibilities = agent_spec.get('responsibilities', [])
        if isinstance(responsibilities, list):
            resp_text = '\n'.join(f"- {r}" for r in responsibilities)
        else:
            resp_text = f"- {responsibilities}"
        
        if not resp_text.strip():
            resp_text = "- Execute assigned tasks\n- Report progress\n- Coordinate with other agents"
        
        # Format capabilities
        capabilities = agent_spec.get('capabilities', [])
        if isinstance(capabilities, list):
            cap_text = '\n'.join(f"- {c}" for c in capabilities)
        else:
            cap_text = f"- {capabilities}"
        
        if not cap_text.strip():
            cap_text = "- Task execution\n- Status reporting\n- Team collaboration"
        
        # Integration points
        agent_type = agent_spec.get('type', 'development')
        integration_text = self._generate_integration_text(agent_type)
        
        # Quality standards
        quality_text = self._generate_quality_standards(agent_type)
        
        # Success metrics
        metrics_text = self._generate_success_metrics(agent_type)
        
        # Related docs
        related_docs = self._generate_related_docs(agent_type)
        
        # Notes
        notes = agent_spec.get('notes', 
            'This agent was generated automatically from project vision analysis.')
        
        # Generate content
        content = self.AGENT_TEMPLATE.format(
            title=agent_spec['title'],
            agent_id=agent_spec['agent_id'],
            role=agent_spec['role'],
            authority=authority.title(),
            authority_description=authority_desc,
            responsibilities=resp_text,
            capabilities=cap_text,
            integration=integration_text,
            quality_standards=quality_text,
            success_metrics=metrics_text,
            related_docs=related_docs,
            notes=notes,
            generated_date=datetime.now().strftime('%Y-%m-%d'),
            source='.mas-system/agent-specifications.yaml'
        )
        
        return content
    
    def save_definition(self, agent_spec: Dict[str, Any]) -> str:
        """Generate and save agent definition file"""
        
        content = self.generate_definition(agent_spec)
        
        # Determine directory based on agent type
        agent_type = agent_spec.get('type', 'development')
        if agent_type == 'enforcement':
            target_dir = self.enforcement_dir
        else:
            target_dir = self.mutagen_dir
        
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filename
        filename = f"{agent_spec['agent_id']}.md"
        filepath = target_dir / filename
        
        # Save file
        with open(filepath, 'w') as f:
            f.write(content)
        
        return str(filepath)
    
    def generate_all(self, spec_file: str = None) -> List[str]:
        """Generate all agent definitions from specifications"""
        
        specs = self.load_specifications(spec_file)
        generated_files = []
        
        print(f"🤖 Generating {len(specs)} agent definitions...\n")
        
        for spec in specs:
            try:
                filepath = self.save_definition(spec)
                generated_files.append(filepath)
                print(f"✅ {spec['title']}")
                print(f"   → {filepath}")
            except Exception as e:
                print(f"❌ {spec.get('title', 'Unknown')} - Error: {e}")
        
        print(f"\n📝 Generated {len(generated_files)} agent definitions")
        return generated_files
    
    def _generate_integration_text(self, agent_type: str) -> str:
        """Generate integration points based on agent type"""
        
        integration_map = {
            'coordination': """
### With Other Agents
- Receives status updates from all development and enforcement agents
- Assigns tasks to development agents
- Coordinates multi-agent workflows
- Escalates blockers to appropriate agents

### With System
- Creates and updates GitHub Issues for coordination
- Triggers workflows as needed
- Maintains shared state in coordination files
""",
            'development': """
### With Coordination Agents
- Receives task assignments
- Reports progress and status
- Requests help when blocked

### With Enforcement Agents
- Submits work for review
- Addresses review feedback
- Ensures compliance with standards

### With Other Development Agents
- Collaborates on complex features
- Hands off work at integration points
- Coordinates on shared components
""",
            'enforcement': """
### With Development Agents
- Reviews submitted work
- Provides feedback and approval/rejection
- Validates compliance with standards

### With Coordination Agents
- Reports enforcement status
- Escalates violations
- Recommends process improvements

### With System
- Automated checks via CI/CD
- Manual reviews via PR comments
- Blocks merge on violations
"""
        }
        
        return integration_map.get(agent_type, integration_map['development'])
    
    def _generate_quality_standards(self, agent_type: str) -> str:
        """Generate quality standards based on agent type"""
        
        standards_map = {
            'coordination': """
- Plans are clear and achievable
- Task assignments are appropriate
- Progress tracking is accurate
- Blockers are resolved quickly
- Communication is timely and clear
""",
            'development': """
- Code follows project standards
- Tests are written and passing
- Documentation is updated
- Changes are minimal and focused
- Work aligns with vision and constitution
""",
            'enforcement': """
- Reviews are thorough and constructive
- Feedback is specific and actionable
- Standards are applied consistently
- False positives are minimized
- Review turnaround is timely
"""
        }
        
        return standards_map.get(agent_type, standards_map['development'])
    
    def _generate_success_metrics(self, agent_type: str) -> str:
        """Generate success metrics based on agent type"""
        
        metrics_map = {
            'coordination': """
- Sprint goals achieved 80%+ of time
- Task assignments appropriate for agent skills
- Blockers resolved within 24 hours
- All agents have clear work assignments
- Progress visible to stakeholders
""",
            'development': """
- Features completed on time
- Code review approval on first submission 80%+
- No critical bugs introduced
- Test coverage maintained/improved
- Documentation updated with changes
""",
            'enforcement': """
- Reviews completed within 4 hours
- Feedback leads to improved quality
- False positive rate < 10%
- Standards violations caught before merge
- Constructive feedback provided
"""
        }
        
        return metrics_map.get(agent_type, metrics_map['development'])
    
    def _generate_related_docs(self, agent_type: str) -> str:
        """Generate related documents links"""
        
        docs_map = {
            'coordination': """
- [Autonomous Sprint Driver](autonomous-sprint-driver.md)
- [Multi-Agent Collaboration](multi-agent-collaboration-agent.md)
- [Task Breakdown Agent](task-breakdown-agent.md)
""",
            'development': """
- [AI Agent Instructions](../../docs/development/ai-agent-instructions.md)
- [Coding Principles](../../docs/development/coding-principles.md)
""",
            'enforcement': """
- [PR Merge Constitution](../pr-merge-constitution.yaml)
- [Constitutional Judge](constitutional-judge-agent.md)
"""
        }
        
        return docs_map.get(agent_type, '')


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate agent definition files')
    parser.add_argument('--repo-root', default=None, help='Repository root path')
    parser.add_argument('--spec-file', default=None, help='Agent specifications YAML file')
    parser.add_argument('--single', default=None, help='Generate single agent by ID')
    
    args = parser.parse_args()
    
    generator = AgentDefinitionGenerator(args.repo_root)
    
    try:
        if args.single:
            # Generate single agent
            specs = generator.load_specifications(args.spec_file)
            agent_spec = next((s for s in specs if s['agent_id'] == args.single), None)
            
            if not agent_spec:
                print(f"❌ Agent not found: {args.single}")
                return 1
            
            filepath = generator.save_definition(agent_spec)
            print(f"✅ Generated: {filepath}")
        else:
            # Generate all agents
            files = generator.generate_all(args.spec_file)
            print(f"\n✅ Complete! Generated {len(files)} files")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
