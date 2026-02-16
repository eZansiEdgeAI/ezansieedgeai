# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) documenting significant architectural decisions made for eZansiEdgeAI.

## What is an ADR?

An Architecture Decision Record (ADR) captures a significant architectural decision along with its context, reasoning, and consequences. ADRs help us:
- Understand why decisions were made
- Evaluate decisions as context changes
- Onboard new contributors
- Avoid revisiting settled decisions
- Learn from past decisions

## Current ADRs

### [ADR-000: Template](ADR-000-template.md)
Template for creating new ADRs. Use this as a starting point for documenting new decisions.

### [ADR-001: Phone-First Architecture](ADR-001-phone-first-architecture.md)
**Status:** Accepted  
**Decision:** The learner's personal Android phone is the primary compute platform, not classroom-based devices or cloud services.

**Key Points:**
- Phones are already owned, trusted, and available
- School infrastructure is unreliable (power, internet, maintenance)
- Lower barrier to adoption and broader reach
- Aligns with mission to serve underserved learners

### [ADR-002: Offline-First Design](ADR-002-offline-first-design.md)
**Status:** Accepted  
**Decision:** The app must work completely offline after initial installation. Online features are optional future enhancements.

**Key Points:**
- Target users face expensive data and inconsistent connectivity
- Core learning experience cannot depend on internet
- Privacy by default (no data transmitted)
- Reliable functionality everywhere

### [ADR-003: Edge Device as Accelerator](ADR-003-edge-device-as-accelerator.md)
**Status:** Accepted  
**Decision:** School edge nodes are optional capability accelerators, not required infrastructure.

**Key Points:**
- Core functionality works without any infrastructure
- Edge nodes provide STT, TTS, content distribution when available
- Graceful enhancement rather than requirement
- Three deployment modes: Phone-only, Phone+Node, Community Hub

### [ADR-004: Content Pack Architecture](ADR-004-content-pack-architecture.md)
**Status:** Planned  
To be created as part of STORY-011

## ADR Lifecycle

ADRs can have the following statuses:

- **Proposed:** Under consideration, not yet accepted
- **Accepted:** Decision made and being implemented
- **Deprecated:** No longer recommended but may still be in use
- **Superseded:** Replaced by a newer ADR (link to replacement)

## When to Create an ADR

Create an ADR for decisions that:
- Impact the overall system architecture
- Have significant consequences if changed later
- Involve trade-offs between different approaches
- Will affect multiple components or teams
- Establish patterns or standards for the project

Examples:
- Technology choices (frameworks, databases, languages)
- Architectural patterns and styles
- API designs and protocols
- Security and privacy approaches
- Performance and scalability strategies

## How to Create an ADR

1. Copy [ADR-000-template.md](ADR-000-template.md)
2. Name it `ADR-XXX-title-in-kebab-case.md` (next sequential number)
3. Fill in all sections:
   - Context: What decision needs to be made and why
   - Options: What alternatives were considered
   - Decision: What was chosen and why
   - Consequences: Positive and negative impacts
4. Submit as part of your PR
5. Update this README with a summary

## ADR Review Process

ADRs should be reviewed by:
1. Technical lead(s)
2. Relevant domain experts
3. At least one other team member

Once accepted, ADRs guide implementation and should only be changed if context significantly changes.

## Related Documentation

- [Architecture Overview](../architecture/README.md) - Technical architecture docs
- [Product Vision](../product/vision.md) - Strategic direction and philosophy
- [Development Backlog](../development/backlog-v1.md) - Implementation roadmap

## Naming Convention

ADRs are numbered sequentially starting from 001:
```
ADR-000-template.md
ADR-001-phone-first-architecture.md
ADR-002-offline-first-design.md
ADR-003-edge-device-as-accelerator.md
...
```

## Format

We use the [MADR (Markdown Architectural Decision Records)](https://adr.github.io/madr/) format with some customization for our needs.

## Questions?

If you have questions about existing ADRs or want to propose a new one, see [CONTRIBUTING.md](../../CONTRIBUTING.md) for how to engage with the team.
