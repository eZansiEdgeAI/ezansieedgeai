# ADR-003: Edge Device as Capability Accelerator (Not Brain)

## Status
accepted

## Context
In designing the school edge node, a fundamental architectural question arose: should the school device be the primary AI processing brain, or an optional enhancer?

Two approaches were considered:

**Option A — Edge Device as Brain**  
The school node hosts the primary AI models. Phones are thin clients that send queries to the node and display responses. The phone alone cannot perform inference.

**Option B — Edge Device as Accelerator**  
The phone is always the primary compute surface (per ADR-001). The school node provides enhanced capabilities — STT, TTS, heavier models, content distribution — but the phone works completely independently without it.

Key contextual factors:
- School electricity supply is unreliable — load shedding cuts power to edge devices
- School IT infrastructure is poorly maintained and often unavailable
- Physical hardware at schools is subject to failure, theft, and damage
- If the brain is in the school and the school is dark, every learner's device stops working
- Phones already run the complete inference stack (per ADR-001 and ADR-002)
- Duplicating inference onto the school device does not reduce the phone-side requirement

## Decision
The school edge device is a capability accelerator, not the AI brain.

The edge node provides:
- Shared Speech-to-Text (STT) for voice input
- Shared Text-to-Speech (TTS) for audio output
- Content pack distribution and updates over LAN
- App and model update distribution over LAN
- Optionally: a larger inference model for complex queries

The phone must be capable of performing all core learning functions without the edge node. The edge node adds quality and convenience — it does not enable core functionality.

If the edge node is offline, unreachable, or absent, the phone continues working silently in offline-only mode. No error is shown to the learner for missing enhanced services.

## Rationale
- Load shedding makes shared hardware unreliable — a brain that goes dark takes every learner offline
- Distributing AI capability to every phone is more resilient than centralising it
- The phone-first architecture (ADR-001) already requires full on-device inference capability
- Making the edge node a dependency contradicts the offline-first principle (ADR-002)
- STT/TTS are the natural services to centralise — they are compute-heavy and not part of the core text-based V1 flow

Rejected alternative: Edge-as-brain was rejected because it introduces a single point of failure for the entire school's learning capability, contradicts the offline-first and phone-first principles, and provides no resilience against load shedding or hardware failure.

## Consequences

### Positive
- Resilient architecture — node failure has no impact on core learning
- Learner experience is consistent regardless of whether the node is present
- Reduces pressure to maintain school hardware reliability
- Enables gradual rollout — schools without nodes still get full V1 functionality
- School node adds value incrementally without creating risk

### Negative / Trade-offs
- Phone-only mode has reduced capabilities: no voice input, no voice output, no access to larger models
- Voice features (STT/TTS) require the school node — some learners may not benefit from them
- Development complexity increases: every feature must be designed to degrade gracefully
- Cannot centralise model updates via the node — phones must receive updates independently
- School node value proposition requires clear communication — it is an enhancement, not a requirement
