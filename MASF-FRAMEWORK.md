# MaSf-vision Framework

This repository uses the MaSf-vision (Multi-Agent System Framework based on vision) framework.

## What is MaSf-vision?

MaSf-vision is a framework that enables autonomous AI agents to understand your project vision,
self-organize, and execute collaboratively to realize that vision.

## Key Components

### 1. Vision Document
Your project vision in `docs/product/vision.md` defines:
- Mission and purpose
- Core principles
- Goals and success criteria
- Constraints

### 2. PR Constitution
Generated from your vision, the PR constitution (`.github/agents/pr-merge-constitution.yaml`)
defines validation rules for pull requests that align with your principles.

### 3. Automated Workflows
GitHub Actions workflows automatically validate PRs against your constitution.

## Usage

### Updating Vision
When your vision evolves, update `docs/product/vision.md` and regenerate the constitution:

```bash
python tools/agent-orchestration/pr-constitution-generator.py
```

### PR Validation
Every PR is automatically checked against your constitution. The workflow will:
1. Validate core principles are followed
2. Check technical requirements
3. Verify code quality
4. Ensure security standards

## Documentation

- [PR Constitution Generator](tools/agent-orchestration/README-pr-constitution.md)
- [Vision Document](docs/product/vision.md)
- [PR Merge Constitution](.github/agents/pr-merge-constitution.yaml)

## Autonomous Agent Execution

The framework includes autonomous agent execution capabilities. For setup instructions:

- **Local Tools**: See tools in `tools/agent-orchestration/`
- **Workflows**: Check `.github/workflows/autonomous-agent-execution.yml`
- **Complete Guide**: Visit the [MaSf-vision Setup Guide](https://github.com/McFuzzySquirrel/MaSf-vision/blob/main/SETUP-AUTONOMOUS-AGENTS.md)

## Learn More

Visit the [MaSf-vision repository](https://github.com/McFuzzySquirrel/MaSf-vision) for more information.
