# ADR-003: Edge Device as Capability Accelerator, Not Core Compute

* **Status:** Accepted
* **Date:** 2026-02-16
* **Decision Makers:** Project Team
* **Technical Story:** Redefining the role of school-based infrastructure

## Context and Problem Statement

Given our decision to build phone-first (ADR-001) and offline-first (ADR-002), we need to decide: **What role, if any, should school-based edge devices play in the architecture?**

The original plan had Raspberry Pi devices as the primary compute platform. With phones now being primary, do we:
- Eliminate school devices entirely?
- Keep them as required infrastructure?
- Redefine their role?

## Decision Drivers

* **Phone-first decision:** Phones are now primary compute platform
* **Offline-first decision:** App must work without any infrastructure
* **School reality:** Many schools have WiFi but it's not always reliable
* **Enhanced capabilities:** Speech services and heavier compute could enhance learning
* **Optional vs required:** Infrastructure should enhance, not gate, the core experience
* **Cost distribution:** Schools should not bear high operational costs
* **Deployment complexity:** Must remain simple to deploy and maintain

## Considered Options

1. **No School Infrastructure:** Phone-only, eliminate school devices entirely
2. **Required School Infrastructure:** Learners must connect to school node to use app
3. **Optional Accelerator:** School node provides enhancements but is not required
4. **Hybrid Mode:** Different features enabled based on infrastructure availability

## Decision Outcome

**Chosen option:** "Optional Accelerator"

School edge devices are **optional capability accelerators**. They provide enhanced services (STT, TTS, heavier models, content distribution) when available, but the core learning experience works completely without them.

**Key principle:** If the school node is offline, removed, or never installed, learners can still learn.

### Reasoning

1. **Preserves mission alignment:** Doesn't exclude learners whose schools lack infrastructure
2. **Graceful enhancement:** Schools with resources can enhance the experience without creating inequality
3. **Reduces deployment friction:** Can deploy to learners immediately without waiting for school infrastructure
4. **Lower risk:** If school device fails, learning continues uninterrupted
5. **Enables future features:** Speech services and larger models possible without requiring them

### Positive Consequences

* **Wider reach:** Works in schools with no infrastructure
* **Lower deployment risk:** Learner app deployment independent of school infrastructure
* **Graceful enhancement:** Better experience when infrastructure available, but not required
* **Future-proof:** Can add more edge services over time without breaking existing deployments
* **Reduced support burden:** Fewer critical dependencies means fewer support calls
* **Cost flexibility:** Schools can choose to add infrastructure based on budget/needs

### Negative Consequences

* **Complex feature matrix:** Need to communicate what works with/without school node
* **Two development paths:** Must develop and test both standalone and enhanced modes
* **Potential confusion:** Users might not understand when/why to connect to school node
* **Delayed speech features:** STT/TTS moved to Phase 3 rather than core V1

## Pros and Cons of the Options

### No School Infrastructure (Eliminate Entirely)

* **Good:** Maximum simplicity
* **Good:** No infrastructure costs ever
* **Good:** One code path to test
* **Bad:** Misses opportunity for schools that want enhanced features
* **Bad:** No path to speech services (compute-intensive)
* **Bad:** Content distribution harder (no local cache)
* **Bad:** Wastes existing school WiFi infrastructure

### Required School Infrastructure

* **Good:** Can rely on infrastructure for compute-heavy tasks
* **Good:** Simpler architecture (single mode)
* **Good:** School-level content management
* **Bad:** Excludes learners whose schools lack infrastructure
* **Bad:** Creates dependency and single point of failure
* **Bad:** Learning stops if infrastructure fails
* **Bad:** Completely misaligned with phone-first decision

### Optional Accelerator (Chosen)

* **Good:** Works everywhere (with or without infrastructure)
* **Good:** Graceful enhancement for schools with resources
* **Good:** Enables advanced features (STT, TTS) without requiring them
* **Good:** Lower risk deployment
* **Good:** Better experience when available, functional without
* **Bad:** More complex to build (two modes)
* **Bad:** Feature matrix communication challenge
* **Bad:** Must design for graceful degradation

### Hybrid Mode

* **Good:** Different features based on availability
* **Good:** Can optimize for each scenario
* **Bad:** Very complex to build and test
* **Bad:** Confusing UX (what's available when?)
* **Bad:** High maintenance burden

## What Edge Nodes Provide (When Available)

### Phase 3+ Features

1. **Content Pack Distribution**
   - Local cache of content packs
   - Fast distribution over LAN (no internet needed)
   - Version management and updates

2. **Speech Services**
   - Speech-to-text (Whisper or similar)
   - Text-to-speech (local TTS)
   - Reduces phone battery usage for these tasks

3. **Compute Offload (Optional)**
   - Larger model inference for complex queries
   - Batch processing
   - Still works if node unavailable

4. **Update Server**
   - Distribute app updates over LAN
   - No internet required

### What Edge Nodes DO NOT Provide

- ❌ Required infrastructure for core functionality
- ❌ Authentication or user management
- ❌ Centralized learner data storage
- ❌ Internet gateway or cloud connectivity
- ❌ Critical dependencies

## Implementation Architecture

### Service Discovery

- **mDNS/Bonjour:** Automatic discovery of school node on local network
- **Manual configuration:** QR code or IP address if auto-discovery fails
- **Graceful fallback:** If not found, app works normally

### API Design

```
Phone App → School Node (if available)
           ↓
       [Faster/Enhanced Features]
           ↓
       Falls back to local if node unreachable
```

### Feature Flags

App should detect node availability and:
- Enable STT/TTS UI if node has speech services
- Offer content pack updates if node has content server
- Fall back to local-only if node unreachable

### Zero-Config Goal

Ideal UX:
1. Learner opens app at school
2. App discovers school node automatically
3. Enhanced features appear
4. At home (no node), app works normally

No configuration required.

## Deployment Modes

### Mode A: Phone Only
- **Scenario:** Home, schools with no infrastructure, community centers
- **Features:** Full core functionality
- **Missing:** STT, TTS, fast content updates

### Mode B: Phone + School Node
- **Scenario:** Schools with WiFi and edge device
- **Features:** Full core + STT + TTS + fast updates
- **Missing:** Nothing (full experience)

### Mode C: Community Hub
- **Scenario:** Library, NGO, shared location with edge device
- **Features:** Same as Mode B
- **Missing:** Nothing

## Development Priority

1. **Phase 1-2:** Phone-only mode (Mode A)
2. **Phase 3:** Add school node (Modes B & C)
3. **Future:** Additional edge services

This ensures we can deploy and validate core functionality before adding infrastructure complexity.

## Links

* [Vision Document - Section 5.3: School Device = Capability Booster](../product/vision.md)
* [Vision Document - Section 6.2: School Edge Device Stack](../product/vision.md)
* [Vision Document - Section 9: Deployment Modes](../product/vision.md)
* [ADR-001: Phone-First Architecture](ADR-001-phone-first-architecture.md)
* [ADR-002: Offline-First Design](ADR-002-offline-first-design.md)
* [Edge Device Architecture](../architecture/edge-device-architecture.md) (to be created)
* [Deployment Modes](../architecture/deployment-modes.md) (to be created)

---

## References

From vision document:

> **5.3 School Device = Capability Booster, Not Brain**  
> Instead of hosting models:  
> School device provides:
> - Speech to Text
> - Text to Speech
> - Content distribution
> - Optional heavier inference
> - Update distribution

> **Important:**  
> If node is offline → learning must still work.

> **9. Deployment Modes**
> 
> **Mode A – Phone Only**  
> Worst case fallback. Still usable.
> 
> **Mode B – Phone + School Edge WiFi**  
> Primary target deployment.

## Notes

This decision reflects a maturation of our thinking. Rather than trying to solve all problems with phone-only or forcing infrastructure requirements, we're creating a gracefully degrading system that works everywhere but is better where resources exist.

This is the "realistic, deployable" approach the vision document calls for.
