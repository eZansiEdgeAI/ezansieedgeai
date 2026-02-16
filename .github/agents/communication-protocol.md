# Agent Communication Protocol (ACP)

## Purpose

This protocol defines how AI agents communicate with each other and with the codebase when working on the MaS project. It ensures consistency, quality, and alignment with project goals.

## Core Principles

### 1. Context Awareness
Agents must understand:
- Project vision and constraints
- Architecture decisions (ADRs)
- Existing code patterns
- User personas and needs

### 2. Collaborative Decision Making
Agents should:
- Consult relevant documentation before major decisions
- Flag architectural changes for review
- Build on existing patterns rather than reinventing
- Communicate tradeoffs clearly

### 3. Quality Gates
All agent work must pass:
- Offline-first validation
- Low-end device compatibility
- Security review
- Performance benchmarks
- Test coverage requirements

## Communication Structure

### Agent Types

#### 1. Enforcement Agents
**Role**: Ensure compliance with project standards

**Agents**:
- Constitutional Judge Agent: Validates against core principles
- Security Enforcement Agent: Checks for vulnerabilities
- Reality Enforcement Agent: Ensures practical, working solutions
- Complexity Enforcement Agent: Prevents over-engineering

**Communication**: Provide clear pass/fail with actionable feedback

#### 2. Mutagen Agents
**Role**: Drive development and collaboration

**Agents**:
- Autonomous Sprint Driver: Plans and executes sprints
- Task Breakdown Agent: Decomposes complex tasks
- Multi-Agent Collaboration Agent: Coordinates multiple agents

**Communication**: Propose plans, coordinate execution, report progress

#### 3. Development Agents
**Role**: Implement features and fixes

**Communication**: Follow coding principles, request reviews, document decisions

## Message Protocol

### Status Reports
```yaml
agent: [agent-name]
task: [task-description]
status: [in-progress|completed|blocked|failed]
progress:
  - completed: [list of completed items]
  - in-progress: [current work]
  - blocked: [blockers if any]
context:
  - [relevant context, decisions, tradeoffs]
```

### Decision Requests
```yaml
agent: [agent-name]
decision_needed: [summary]
options:
  - option_1:
      description: [description]
      pros: [benefits]
      cons: [drawbacks]
  - option_2:
      description: [description]
      pros: [benefits]
      cons: [drawbacks]
recommendation: [option with rationale]
references:
  - [relevant ADRs, docs, constraints]
```

### Code Review Requests
```yaml
agent: [agent-name]
change_type: [feature|fix|refactor|docs]
scope: [affected components]
summary: [what changed and why]
offline_tested: [yes|no]
device_tested: [device specs]
tests_added: [yes|no]
breaking_changes: [yes|no - with explanation]
```

## Workflow

### 1. Task Initiation
```
Task Assigned
    ↓
Read Context (vision, ADRs, constraints)
    ↓
Explore Codebase
    ↓
Propose Plan
    ↓
Get Approval (if architectural)
    ↓
Execute
```

### 2. During Execution
```
Implement Change
    ↓
Self-Review
    ↓
Test Offline
    ↓
Test on Target Device
    ↓
Run Tests
    ↓
Request Enforcement Review
    ↓
Address Feedback
    ↓
Commit
```

### 3. Completion
```
Final Testing
    ↓
Documentation Update
    ↓
Status Report
    ↓
Handoff/Close
```

## Quality Gates

### Must Pass Before Commit

1. **Offline-First Check**
   - Feature works with airplane mode on
   - No blocked UI on network requests
   - Graceful handling of network failures

2. **Device Compatibility**
   - Tested on low-end device (2GB RAM)
   - Performance within targets
   - No crashes or memory leaks

3. **Security Check**
   - No hardcoded secrets
   - Sensitive data encrypted
   - Input validation present
   - No known vulnerabilities

4. **Code Quality**
   - Follows coding principles
   - Tests written and passing
   - Documentation updated
   - No unnecessary complexity

5. **Architecture Alignment**
   - Consistent with ADRs
   - Mobile-first approach
   - Edge device optional
   - Follows existing patterns

## Enforcement Points

### Pre-Commit
- Linting
- Unit tests
- Security scans
- Complexity analysis

### Pre-PR
- Integration tests
- Offline scenarios
- Device compatibility
- Documentation review

### Pre-Merge
- Constitutional review
- Security audit
- Reality check
- Complexity evaluation

## Agent Coordination

### When Multiple Agents Work Together

#### Planning Phase
1. Primary agent proposes overall plan
2. Specialized agents review their areas
3. Consensus on approach
4. Clear responsibility assignment

#### Execution Phase
1. Parallel work on independent components
2. Regular sync points
3. Integration testing
4. Collaborative problem-solving

#### Review Phase
1. Self-review by implementing agent
2. Peer review by development agents
3. Enforcement agent validation
4. Collective approval

## Communication Channels

### In Code
- Comments for complex logic
- ADRs for architectural decisions
- Inline documentation for APIs
- Commit messages for changes

### In PRs
- Clear description of changes
- Rationale for approach
- Test evidence
- Breaking change notes

### In Issues
- Context and background
- Acceptance criteria
- Constraints and considerations
- Links to related items

## Decision Authority

### Agent Can Decide
- Implementation details
- Code structure within file
- Variable/function names
- Test structure
- Minor optimizations

### Agent Should Propose
- New dependencies
- Architectural patterns
- API designs
- Database schema changes
- Breaking changes

### Human Must Decide
- Major architectural shifts
- Changes to core principles
- Security policy changes
- Release decisions
- Budget/resource allocation

## Error Handling

### When Agent Gets Stuck
1. Document what was attempted
2. Explain why it didn't work
3. Describe blockers
4. Propose alternatives
5. Request guidance

### When Agent Makes Mistake
1. Acknowledge error
2. Explain what went wrong
3. Describe corrective action
4. Implement fix
5. Add test to prevent recurrence

## Success Criteria

An agent has successfully completed a task when:
- Feature works offline as specified
- Tests pass on target devices
- Documentation is updated
- Enforcement agents approve
- Code merged to main branch

## Continuous Improvement

### Feedback Loop
- Agents learn from reviews
- Patterns codified in documentation
- Common issues addressed systematically
- Protocol updated based on experience

### Metrics
- First-time approval rate
- Rework frequency
- Time to completion
- Quality indicators

## Related Documents

- [PR Merge Constitution](pr-merge-constitution.yaml)
- [AI Agent Instructions](../docs/development/ai-agent-instructions.md)
- [Coding Principles](../docs/development/coding-principles.md)
