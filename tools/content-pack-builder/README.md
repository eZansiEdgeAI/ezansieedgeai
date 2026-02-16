# Content Pack Builder

## Overview

Tools for creating, packaging, and validating educational content for offline distribution in the MaS platform.

## Purpose

Content creators need to:
- Author educational content
- Package content for offline use
- Optimize assets (images, videos)
- Generate metadata
- Validate content packages
- Version content

## Features

### Content Authoring
- Markdown-based lesson creation
- Interactive element definition
- Assessment creation
- Media asset management

### Content Packaging
- Bundle content into .mas packages
- Compress assets efficiently
- Generate manifests
- Sign packages
- Version management

### Asset Optimization
- Image compression
- Video transcoding
- Audio optimization
- Size validation

### Validation
- Content structure validation
- Metadata verification
- Asset integrity checks
- Size compliance
- Accessibility checks

## Content Package Format

```
content-package.mas
├── manifest.json         # Package metadata
├── content/
│   ├── lessons/         # Lesson files
│   ├── assessments/     # Quiz/test files
│   └── resources/       # Reference materials
├── assets/
│   ├── images/
│   ├── videos/
│   └── audio/
└── signature.sig        # Package signature
```

## Manifest Structure

```json
{
  "id": "package-id",
  "version": "1.0.0",
  "title": "Package Title",
  "description": "Package description",
  "language": "en",
  "subject": "mathematics",
  "grade_level": "5-6",
  "size": 12345678,
  "lessons": [],
  "assessments": [],
  "dependencies": [],
  "created": "2026-02-16T00:00:00Z"
}
```

## CLI Tool

```bash
# Create new package
mas-pack create --title "Grade 5 Math" --subject math

# Add lesson
mas-pack add-lesson lessons/fractions.md

# Add assessment
mas-pack add-assessment assessments/quiz1.yaml

# Optimize assets
mas-pack optimize --quality medium

# Validate package
mas-pack validate

# Build package
mas-pack build --output math-grade5.mas

# Sign package
mas-pack sign --key signing-key.pem
```

## Content Authoring Format

### Lesson (Markdown)
```markdown
---
id: lesson-001
title: Introduction to Fractions
duration: 30
---

# Introduction to Fractions

## Learning Objectives
- Understand what fractions are
- Identify numerator and denominator
- Compare simple fractions

## Content
...
```

### Assessment (YAML)
```yaml
id: quiz-001
title: Fractions Quiz
questions:
  - type: multiple_choice
    question: "What is 1/2 + 1/4?"
    options:
      - "1/6"
      - "3/4"
      - "2/6"
      - "1/3"
    correct: 1
```

## Size Guidelines

- Total package: < 500MB
- Single lesson: < 5MB
- Single video: < 20MB
- Single image: < 500KB
- Single audio: < 2MB

## Development

### Prerequisites
(To be added)

### Installation
(To be added)

### Usage
(To be added)

## Testing

- Content validation tests
- Package integrity tests
- Size compliance tests
- Format compatibility tests

## Related Documents

- [Content Authoring Guide](../../docs/content/authoring-guide.md) (to be created)
- [Content Specifications](../../docs/content/specifications.md) (to be created)
- [Coding Principles](../../docs/development/coding-principles.md)
