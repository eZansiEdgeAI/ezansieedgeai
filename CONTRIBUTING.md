# Contributing to eZansiEdgeAI

Thank you for your interest in contributing to eZansiEdgeAI! This project aims to provide AI-powered learning support to underserved learners, and we welcome contributions from developers, educators, content creators, and anyone passionate about educational equity.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Submitting Changes](#submitting-changes)
- [Architecture Decision Records](#architecture-decision-records)
- [Documentation](#documentation)

## Code of Conduct

This project is dedicated to providing a welcoming and inclusive experience for everyone. We expect all contributors to:

- Be respectful and considerate
- Welcome diverse perspectives
- Focus on what's best for the community and learners
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

If you find a bug:
1. Check if it's already reported in [Issues](https://github.com/eZansiEdgeAI/ezansieedgeai/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Device/OS information
   - Screenshots if applicable

### Suggesting Features

Feature suggestions are welcome! Please:
1. Check existing issues and discussions first
2. Consider alignment with our [Vision](docs/product/vision.md) and constraints
3. Open an issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Alternatives you've considered
   - How it fits with offline-first, phone-first design

### Contributing Code

1. **Pick a task:** Check the [backlog](docs/development/backlog-v1.md) or issues labeled `good-first-issue`
2. **Discuss first:** For significant changes, open an issue to discuss before coding
3. **Follow standards:** See [Coding Standards](#coding-standards) below
4. **Write tests:** All code should include appropriate tests
5. **Update docs:** Keep documentation in sync with code changes

### Contributing Content

Educational content contributions are valuable! If you want to contribute curriculum content:
1. Ensure content is properly licensed (open/creative commons)
2. Align with CAPS curriculum (South African curriculum)
3. Follow content pack format (see [Content Pack Schema](docs/architecture/content-pack-schema.md) when available)
4. Include worked examples and explanations

## Development Setup

### Prerequisites

- **For Android App:**
  - Android Studio Arctic Fox or later
  - Kotlin 1.9+
  - Android SDK (API 29+)

- **For Python Tools:**
  - Python 3.11+
  - pip
  - virtualenv

- **For Edge Node (future):**
  - Linux environment (or WSL on Windows)
  - Python or Go (TBD)

### Getting Started

1. **Fork and clone:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/ezansieedgeai.git
   cd ezansieedgeai
   ```

2. **Create a branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Set up Python environment (for tools):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Make your changes**

5. **Test your changes** (see below)

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**

## Coding Standards

### General Principles

1. **Offline-First:** All code must work without internet connectivity
2. **Privacy-First:** No data collection without explicit user consent
3. **Resource-Conscious:** Optimize for low-end devices (3GB RAM)
4. **Simple & Clear:** Code should be readable and maintainable
5. **Well-Documented:** Comment complex logic, update docs

### Kotlin (Android App)

- Use Kotlin style guide
- Follow MVVM architecture pattern
- Use Jetpack components where appropriate
- Write unit tests for ViewModels and business logic
- Write UI tests for critical user flows

### Python (Tools & Scripts)

- Follow PEP 8 style guide
- Use type hints
- Write docstrings for public functions
- Include unit tests (pytest)
- Use meaningful variable names

### Documentation

- Use Markdown for all documentation
- Keep line length reasonable (80-100 characters when practical)
- Include examples where helpful
- Update relevant docs when changing code

## Testing

### Required Tests

- **Unit Tests:** For all business logic
- **Integration Tests:** For component interactions
- **UI Tests:** For critical user flows
- **Offline Tests:** Test ALL functionality in airplane mode
- **Low-Resource Tests:** Test on 3GB RAM device or emulator

### Running Tests

```bash
# Python tests
pytest

# Android tests (from Android Studio or command line)
./gradlew test
./gradlew connectedAndroidTest
```

## Submitting Changes

### Pull Request Process

1. **Ensure CI passes:** All tests must pass
2. **Update documentation:** Keep docs in sync
3. **One feature per PR:** Keep PRs focused and reviewable
4. **Link to issue:** Reference related issue number
5. **Describe changes:** Clear description of what and why

### PR Template

When opening a PR, please include:

```markdown
## Description
[Clear description of changes]

## Related Issue
Fixes #[issue-number]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (describe)

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Tested on Android device
- [ ] Tested in airplane mode (offline)
- [ ] Tested on low-RAM device (3GB)

## Documentation
- [ ] Code comments added/updated
- [ ] README updated (if applicable)
- [ ] Architecture docs updated (if applicable)
- [ ] ADR created (if architectural decision made)

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Tests pass locally
- [ ] Documentation is clear and complete
```

## Architecture Decision Records

For significant architectural changes:

1. Create an ADR using the [template](docs/adr/ADR-000-template.md)
2. Number it sequentially (ADR-XXX)
3. Include it in your PR
4. Update [docs/adr/README.md](docs/adr/README.md)

See [existing ADRs](docs/adr/) for examples.

## Documentation

All documentation lives in the `docs/` directory:

- `docs/product/` - Product vision, requirements, personas
- `docs/architecture/` - Technical architecture
- `docs/adr/` - Architecture Decision Records
- `docs/development/` - Development guides, backlog

When adding/updating docs:
- Keep them synchronized with code
- Use clear, simple language
- Include examples
- Link related documents

## Review Process

All contributions go through review:

1. **Automated checks:** CI must pass (tests, linting)
2. **Code review:** At least one maintainer reviews
3. **Testing:** Reviewer may test on actual device
4. **Documentation review:** Ensure docs are clear and complete

Reviews typically happen within a few days. Be patient and responsive to feedback!

## Questions?

- **General questions:** Open a [Discussion](https://github.com/eZansiEdgeAI/ezansieedgeai/discussions)
- **Bug reports:** Open an [Issue](https://github.com/eZansiEdgeAI/ezansieedgeai/issues)
- **Security issues:** Email [security contact - TBD]

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (to be determined - likely Apache 2.0 or MIT).

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Project documentation where appropriate

Thank you for contributing to making education more accessible! 🎓
