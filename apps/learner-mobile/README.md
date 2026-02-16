# eZansiEdgeAI Learner Mobile App

Android application providing offline AI-powered learning support for learners.

## Overview

The learner mobile app is the primary interface for the eZansiEdgeAI system. It enables learners to:
- Ask questions about their curriculum content offline
- Receive grounded explanations from local content packs
- Access worked examples and learning materials
- Customize their learning preferences
- Work completely offline after initial setup

## Technical Specifications

- **Platform:** Android
- **Minimum SDK:** Android 10 (API 29)
- **Target SDK:** Android 14 (API 34)
- **Language:** Kotlin
- **UI Framework:** Jetpack Compose (planned)
- **Architecture:** MVVM with offline-first design

## Key Components (Planned)

### 1. Content Pack Manager
- Load and manage offline content packs
- Validate pack integrity
- Handle version updates

### 2. Retrieval Engine
- Generate query embeddings
- Perform vector similarity search
- Rank and retrieve relevant content

### 3. AI Inference Engine
- On-device LLM inference
- Prompt template management
- Response generation

### 4. Learner Profile Manager
- Store learning preferences locally
- Manage customization settings
- Privacy-first design (no tracking)

### 5. User Interface
- Question input
- Explanation display
- History/bookmarks
- Settings and preferences

## Device Requirements

- **RAM:** 3GB minimum
- **Storage:** 500MB for app + content pack
- **OS:** Android 10 or higher
- **Architecture:** ARM64 (primary), x86_64 (secondary)

## Development Status

🚧 **Status:** Planning/Foundation Phase

Currently defining architecture and establishing development infrastructure.

## Setup Instructions

*Coming soon - Android project not yet initialized*

## Related Documentation

- [Phone Architecture](../../docs/architecture/phone-architecture.md)
- [Content Pack Schema](../../docs/architecture/content-pack-schema.md)
- [ADR-001: Phone-First Architecture](../../docs/adr/ADR-001-phone-first-architecture.md)
- [ADR-002: Offline-First Design](../../docs/adr/ADR-002-offline-first-design.md)

## Contributing

Please see [CONTRIBUTING.md](../../CONTRIBUTING.md) for development guidelines and how to contribute to this project.

## License

*To be added - Open source license*
