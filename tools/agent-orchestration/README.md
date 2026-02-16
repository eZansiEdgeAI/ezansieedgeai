# Agent Orchestration System

This directory contains tools for autonomous agent coordination and execution in the MaSf-vision project.

## Overview

The agent orchestration system enables AI agents to self-organize and execute tasks autonomously based on the project vision and backlog. It provides:

1. **Vision-Based Task Extraction**: Automatically generates sprint plans from vision and backlog
2. **Agent Self-Creation**: Allows agents to create new specialized agent definitions as needed
3. **Autonomous Execution**: Coordinates agent execution through GitHub workflows
4. **ADR Auto-Generation**: Detects when architectural decisions need documentation

## Components

### 1. Vision Task Extractor (`vision-task-extractor.py`)

Parses the project vision and backlog to extract actionable tasks and generate sprint plans.

**Usage:**
```bash
python vision-task-extractor.py --repo-root /path/to/repo
```

**Output:**
- `current-sprint.yaml`: Sprint plan with tasks, priorities, and agent assignments

**Features:**
- Extracts tasks from backlog epics
- Aligns with vision goals
- Suggests appropriate agent types
- Estimates story points
- Prioritizes based on epic priority

### 2. Agent Creator (`agent-creator.py`)

Analyzes task patterns and creates specialized agent definitions when needed.

**Usage:**
```bash
# Analyze task patterns
python agent-creator.py --action analyze --sprint-plan current-sprint.yaml

# Suggest agent creations
python agent-creator.py --action suggest --sprint-plan current-sprint.yaml

# Create agent from specification
python agent-creator.py --action create --agent-spec agent-spec.json
```

**Features:**
- Identifies high-volume task types
- Proposes specialized agents
- Generates agent definition files
- Maintains consistency with existing agents

### 3. Agent Definition Generator (`agent-definition-generator.py`)

Generates agent definition markdown files from specifications.

**Usage:**
```bash
# Generate all agents from specifications
python agent-definition-generator.py

# Generate specific agent
python agent-definition-generator.py --single master-coordinator

# Use custom spec file
python agent-definition-generator.py --spec-file /path/to/specs.yaml
```

**Output:**
- Creates `.md` files in `.github/agents/mutagen-agents/` or `enforcement-agents/`
- Each file contains role, responsibilities, communication protocols, etc.

**Features:**
- Converts YAML specs to formatted markdown
- Adds appropriate integration points by agent type
- Includes quality standards and success metrics
- Links to related documentation

### 4. Autonomous Agent Execution Workflow

GitHub Actions workflow that orchestrates autonomous execution.

**Trigger:**
```bash
# Manual trigger
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning

# Scheduled: Runs weekly on Monday at 9 AM UTC
```

**Modes:**
- `sprint-planning`: Generate sprint plan from vision
- `execute-tasks`: Coordinate agent task execution
- `create-adr`: Detect and create ADRs
- `full-autonomous`: Run all modes

## How It Works

### 1. Sprint Planning Phase

```
Vision + Backlog → Task Extraction → Sprint Plan → Issue Creation
```

1. Reads `docs/product/vision.md` for goals and principles
2. Parses `docs/development/backlog-v1.md` for epics and stories
3. Extracts actionable tasks with metadata
4. Generates sprint plan aligned with vision
5. Creates GitHub issue with sprint plan

### 2. Agent Creation Phase

```
Sprint Plan → Task Analysis → Agent Suggestions → Agent Creation
```

1. Analyzes task types and volumes
2. Identifies need for specialized agents
3. Proposes agent specifications
4. Creates agent definition files
5. Registers agents in coordination system

### 3. Execution Phase

```
Sprint Plan → Task Assignment → Agent Execution → Progress Tracking
```

1. Agents pick up assigned tasks
2. Execute according to their definitions
3. Report progress via issues/PRs
4. Coordinate through shared state
5. Generate ADRs for decisions

### 4. ADR Detection Phase

```
Code Changes → Decision Detection → ADR Generation → Documentation
```

1. Monitors commits for architectural keywords
2. Detects when ADRs are needed
3. Triggers ADR generation workflow
4. Creates issues for missing ADRs

## Configuration

### Sprint Plan Format

```yaml
sprint_goal: "Deliver core functionality"
duration_days: 14
epics:
  - id: "Epic 1"
    title: "Mobile Application Core"
    priority: "Critical"
    goal: "Functional mobile app"
    stories: [...]
alignment:
  vision_goals: [...]
  success_criteria: [...]
tasks:
  - id: "TASK-001"
    description: "Implement feature X"
    agent_type: "ui-agent"
    priority: "Critical"
    status: "todo"
    estimated_points: 3
```

### Agent Specification Format

```json
{
  "agent_id": "ui-development-agent",
  "title": "UI Development Agent",
  "role": "Develop user interface components",
  "type": "mutagen",
  "authority_level": "Implement",
  "responsibilities": [
    "Implement UI components",
    "Ensure mobile-first design"
  ],
  "capabilities": [
    "React Native development",
    "Mobile UI/UX"
  ]
}
```

## Agent Types

The system recognizes and suggests these agent types:

- **ui-agent**: UI/UX implementation
- **data-agent**: Data layer and storage
- **test-agent**: Testing and QA
- **doc-agent**: Documentation
- **backend-agent**: API and services
- **general-agent**: General development

## Integration with Existing Agents

This orchestration system works with the existing agent definitions:

### Mutagen Agents
- **Autonomous Sprint Driver**: Uses sprint plans to drive execution
- **Multi-Agent Collaboration**: Coordinates between specialized agents
- **Task Breakdown Agent**: Decomposes tasks further if needed

### Enforcement Agents
- **Constitutional Judge**: Validates against principles
- **Reality Enforcement**: Ensures practical solutions
- **Security Enforcement**: Checks for vulnerabilities
- **Complexity Enforcement**: Prevents over-engineering

## Workflow Examples

### Example 1: Starting a New Sprint

```bash
# 1. Generate sprint plan
python vision-task-extractor.py

# 2. Review generated plan
cat current-sprint.yaml

# 3. Trigger autonomous execution
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous

# 4. Monitor progress
gh issue list --label "autonomous-agent"
```

### Example 2: Creating Specialized Agents

```bash
# 1. Analyze current sprint needs
python agent-creator.py --action suggest

# 2. Review suggestions
# (Output shows recommended agent creations)

# 3. Create agents automatically
python agent-creator.py --action create --agent-spec ui-agent-spec.json

# 4. New agents are now available for task assignment
```

### Example 3: ADR Auto-Detection

```bash
# Workflow runs automatically on schedule
# Or trigger manually:
gh workflow run autonomous-agent-execution.yml -f mode=create-adr

# Review ADR suggestions
gh issue list --label "adr"
```

## Best Practices

### For Vision Updates
- Update `docs/product/vision.md` to reflect current goals
- Keep short-term goals specific and measurable
- Update success criteria regularly

### For Backlog Management
- Keep epics focused and scoped
- Mark priorities clearly (Critical/High/Medium/Low)
- Break down stories into discrete tasks
- Use checkboxes for task lists

### For Agent Creation
- Create specialized agents only when task volume justifies it
- Ensure new agents align with project principles
- Document agent capabilities clearly
- Test agent definitions before deployment

### For Autonomous Execution
- Review sprint plans before execution
- Monitor agent coordination issues
- Address blockers promptly
- Validate ADR suggestions

## Monitoring and Debugging

### Check Sprint Plan
```bash
cat tools/agent-orchestration/current-sprint.yaml
```

### View Agent Suggestions
```bash
python agent-creator.py --action suggest
```

### Check Workflow Status
```bash
gh run list --workflow=autonomous-agent-execution.yml
```

### Review Agent Activity
```bash
gh issue list --label "agent-execution"
```

## Troubleshooting

### Sprint Plan Not Generated
- Check that `docs/product/vision.md` exists
- Check that `docs/development/backlog-v1.md` exists
- Verify Python and PyYAML are installed

### Agent Creation Fails
- Verify sprint plan exists
- Check agent specification format
- Ensure write permissions to `.github/agents/`

### Workflow Not Triggering
- Check workflow permissions (contents: write, pull-requests: write)
- Verify cron schedule in workflow file
- Check GitHub Actions are enabled

## Future Enhancements

- [ ] Real-time agent coordination via API
- [ ] Agent performance metrics and optimization
- [ ] Automatic task reassignment on blockers
- [ ] Machine learning for task estimation
- [ ] Agent learning from past executions
- [ ] Cross-repository agent coordination

## Related Documentation

- [Communication Protocol](../../.github/agents/communication-protocol.md)
- [Autonomous Sprint Driver](../../.github/agents/mutagen-agents/autonomous-sprint-driver.md)
- [Multi-Agent Collaboration](../../.github/agents/mutagen-agents/multi-agent-collaboration-agent.md)
- [Product Vision](../../docs/product/vision.md)
- [Backlog](../../docs/development/backlog-v1.md)

## Contributing

When enhancing the orchestration system:
1. Maintain alignment with vision and principles
2. Keep agents simple and focused
3. Document changes clearly
4. Test thoroughly before deployment
5. Update this README

---

**Note**: This is an experimental system for autonomous agent coordination. Review all generated plans and agent definitions before approving for execution.
