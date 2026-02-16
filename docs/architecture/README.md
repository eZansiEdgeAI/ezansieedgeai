# Architecture Documentation

This directory contains the technical architecture documentation for eZansiEdgeAI.

## Overview

eZansiEdgeAI uses a **phone-first, offline-first architecture** to provide AI-powered learning support to underserved learners in South Africa and beyond.

## Core Architectural Principles

1. **Phone-First:** The learner's Android phone is the primary compute platform
2. **Offline-First:** All core functionality works without internet connectivity
3. **Privacy-First:** All learner data stays on device
4. **Low-Resource:** Optimized for 3GB RAM Android devices
5. **Content-Grounded:** AI explanations based on local curriculum content, not model memory

## Architecture Documents

### System Overview (To be created)
High-level system architecture, component interaction, and data flow.

**Status:** Planned (STORY-002)

### Phone Architecture (To be created)
Detailed architecture of the learner mobile app including:
- App layer structure
- AI/ML components
- Data storage and retrieval
- Resource optimization

**Status:** Planned (STORY-002)

### Edge Device Architecture (To be created)
Architecture of optional school edge nodes including:
- Service layer design
- API specifications
- Discovery mechanisms
- Deployment options

**Status:** Planned (STORY-002)

### Deployment Modes (To be created)
Three deployment scenarios:
- Mode A: Phone only
- Mode B: Phone + School edge node
- Mode C: Community hub

**Status:** Planned (STORY-002)

### Content Pack Schema (To be created)
Specification for content pack structure, metadata, and versioning.

**Status:** Planned (STORY-011)

### Model Selection Research (To be created)
Research comparing on-device ML options (GGUF, ONNX, TFLite) and model candidates.

**Status:** Planned (STORY-004)

### Storage Analysis (To be created)
Analysis of storage requirements for models, content, and data.

**Status:** Planned (STORY-006)

## Related Documentation

- [Product Vision](../product/vision.md) - Strategic direction and philosophy
- [Architecture Decision Records](../adr/) - Key architectural decisions with rationale
- [Development Backlog](../development/backlog-v1.md) - Implementation roadmap

## Key Decisions

See ADRs for detailed rationale:
- [ADR-001: Phone-First Architecture](../adr/ADR-001-phone-first-architecture.md)
- [ADR-002: Offline-First Design](../adr/ADR-002-offline-first-design.md)
- [ADR-003: Edge Device as Accelerator](../adr/ADR-003-edge-device-as-accelerator.md)

## Technology Stack (Planned)

### Mobile App
- **Platform:** Android 10+ (API 29+)
- **Language:** Kotlin
- **UI:** Jetpack Compose
- **ML Framework:** llama.cpp (GGUF) or ONNX Runtime Mobile
- **Storage:** SQLite + Room, with vector search extension
- **Architecture Pattern:** MVVM

### Edge Node (Future)
- **Platform:** Linux (Debian/Ubuntu)
- **Language:** Python or Go (TBD)
- **Services:** HTTP/gRPC APIs
- **Discovery:** mDNS/Bonjour

## Development Phases

### Phase 0: Feasibility (Weeks 1-2)
Validate technical approach through research and prototypes

### Phase 1: Offline Learning Loop (Weeks 3-6)
Build core question → retrieval → explanation pipeline

### Phase 2: Content + Personalization (Weeks 7-10)
Real content packs and learner preferences

### Phase 3: School Node (Weeks 11-13)
Optional edge device services

## Contributing

When adding architecture documentation:
1. Start from the vision document principles
2. Reference relevant ADRs
3. Include diagrams where helpful (ASCII art, Mermaid, or images)
4. Keep documentation in sync with implementation
5. Update this README with links to new documents

## Diagram Standards

We use the following formats:
- **ASCII art:** For simple diagrams that render in plaintext
- **Mermaid:** For flowcharts, sequence diagrams (renders in GitHub)
- **Images:** For complex architecture diagrams (store in docs/images/)

## Questions or Clarifications

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for how to ask questions or propose changes to the architecture.
