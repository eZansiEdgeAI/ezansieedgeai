# PR Constitution Generator

## Overview

The PR Constitution Generator is a tool that automatically generates a Pull Request validation constitution based on your project's vision document. This ensures that PR validation is aligned with YOUR project's specific principles and requirements, rather than being hardcoded to a specific domain.

## Why This Matters

In a multi-agent framework that can work with ANY vision (education, healthcare, finance, etc.), the PR validation should adapt to the specific principles of each project. Previously, the PR validation was hardcoded for an education platform with specific checks like "offline-first" and "phone-first". Now, it dynamically generates validation rules from your vision.

## How It Works

1. **Reads your vision document** (`docs/product/vision.md`)
2. **Extracts key elements**:
   - Core principles (e.g., "Learner First", "Simplicity", "Privacy")
   - Technical requirements (e.g., device compatibility, performance)
   - Domain context (education, healthcare, etc.)
   - Success criteria
3. **Generates a PR constitution** (`.github/agents/pr-merge-constitution.yaml`) with:
   - Vision-specific core principles
   - Appropriate validation checks
   - Technical requirements based on constraints
   - Generic code quality standards

## Usage

### Generate Constitution

```bash
# Generate constitution from vision
python tools/agent-orchestration/pr-constitution-generator.py

# Specify custom output location
python tools/agent-orchestration/pr-constitution-generator.py \
    --output .github/agents/pr-merge-constitution.yaml

# Dry-run to preview without saving
python tools/agent-orchestration/pr-constitution-generator.py --dry-run
```

### Command Line Options

- `--repo-root`: Repository root directory (default: current directory)
- `--output`, `-o`: Output file path (default: `.github/agents/pr-merge-constitution.yaml`)
- `--dry-run`: Generate but don't save to file

## Vision Document Requirements

Your vision document should include sections for:

1. **Mission/Purpose**: What your project aims to achieve
2. **Guiding Principles**: Core principles that guide decisions
3. **Constraints**: Technical or resource constraints
4. **Success Criteria**: What defines success
5. **Goals**: Short-term and long-term objectives

### Example Vision Structure

```markdown
## Mission Statement
To democratize quality education...

## Guiding Principles
1. **Learner First**: Every decision prioritizes learner experience
2. **Accessibility**: Works for anyone, anywhere
3. **Simplicity**: Easy to use with minimal training
4. **Reliability**: Works consistently in any environment
5. **Privacy**: Learner data is protected and secure
6. **Open**: Open standards, interoperable, community-driven

## Constraints
- Must work on low-spec devices (2GB RAM, Android 8+)
- Limited bandwidth environments
- Offline-capable

## Success Criteria
- 99%+ uptime in offline mode
- Works on 3+ year old devices
- Teachers can deploy without IT support
```

## Generated Constitution

The generated constitution includes:

### Core Principles
- Derived from your vision's guiding principles
- Each principle gets specific validation checks
- Enforcement level: mandatory

### Technical Requirements
- Device compatibility (if mobile/device mentioned)
- Performance requirements (if mentioned in vision)
- Resource constraints (storage, memory, etc.)

### Code Quality Standards
- Testing requirements
- Documentation requirements
- Code style guidelines
- (Generic across all projects)

### Security Requirements
- Data protection
- Privacy (if emphasized in vision)
- Standard security practices

### Architecture Alignment
- Vision compliance checks
- Pattern consistency
- (Ensures changes align with vision)

## Integration with PR Workflow

The PR evaluation workflow (`.github/workflows/pr-evaluation.yml`) reads the generated constitution and:

1. **Constitutional Review**: Checks PRs against core principles
2. **Reality Check**: Validates evidence of testing and implementation
3. **Complexity Check**: Ensures code simplicity
4. **Automated Checks**: Linting, tests, security scans

The workflow is vision-agnostic and adapts to whatever constitution was generated.

## Examples

### Education Platform
Constitution includes principles like:
- Learner First
- Accessibility
- Offline-capable
- Works on low-spec devices

### Healthcare System
Constitution might include:
- Patient Privacy
- HIPAA Compliance
- Data Security
- Reliability
- Audit Trail

### E-commerce Platform
Constitution might include:
- User Experience
- Transaction Security
- Performance
- Scalability

## Customization

After generation, you can manually edit the constitution to:
- Add domain-specific checks
- Adjust enforcement levels
- Add custom validation rules
- Refine principle descriptions

The generator provides a solid starting point that you can tailor to your needs.

## Regeneration

You can regenerate the constitution at any time:
- When your vision evolves
- When you add new principles
- When requirements change

Simply run the generator again, and it will create an updated constitution based on the current vision.

## Best Practices

1. **Keep vision up-to-date**: The constitution is only as good as your vision
2. **Review generated constitution**: Always review and adjust if needed
3. **Communicate changes**: When regenerating, inform team of updates
4. **Version control**: Commit both vision and constitution together
5. **Document deviations**: If you manually modify the constitution, document why

## Troubleshooting

### No principles extracted
- Check that your vision has a "Guiding Principles" or "Principles" section
- Ensure principles are in a numbered or bulleted list
- Verify the section heading contains the word "principle"

### Missing technical requirements
- Add a "Constraints" or "Technical Requirements" section
- Mention devices, performance, storage explicitly
- Use keywords like "mobile", "offline", "performance"

### Too generic
- Add more specific principles to your vision
- Include domain-specific requirements
- Be explicit about what matters most

## See Also

- [Master Agent](./README.md): Full framework documentation
- [Vision Example](../../docs/product/vision.md): Sample vision document
- [PR Workflow](../../.github/workflows/pr-evaluation.yml): How constitution is used
