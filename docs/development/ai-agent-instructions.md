# eZansiEdgeAI: AI Agent Instructions

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** AI Coding Agents, Automated Development Systems

---

## 1. Purpose

This document provides instructions for AI coding agents working on the eZansiEdgeAI project. Read this before making any code or architecture decisions. These instructions are non-negotiable constraints, not suggestions.

---

## 2. Before You Start

Before implementing anything, read:

1. [`docs/product/vision.md`](../product/vision.md) — Mission, philosophy, and strategic direction
2. [`docs/product/constraints.md`](../product/constraints.md) — Non-negotiable constraints
3. [`docs/architecture/system-overview.md`](../architecture/system-overview.md) — System architecture
4. Relevant ADRs in [`docs/adr/`](../adr/) — Documented architectural decisions

If your planned implementation conflicts with any of these documents, stop and flag the conflict rather than proceeding.

---

## 3. Non-Negotiable Rules

### 3.1 Always Prioritise Offline Capability
- Every feature must work with zero network connectivity
- If you are implementing something that requires a network call for core function, you are building the wrong thing
- Optional enhancements (STT, TTS, content sync) may use the LAN — but must degrade gracefully to offline-only
- Test your implementation mentally: "Does this work with airplane mode on?"

### 3.2 V1 Scope Is Grade 6 Mathematics Only — Do Not Expand
- The current scope is explicitly: **Grade 6 Mathematics, CAPS aligned, text interface, offline only**
- Do not implement features for other grades, other subjects, or voice-first interfaces in V1
- If a task seems to require expanding scope, flag it — do not implement it
- Scope discipline is how V1 ships. Expansion comes after proven real-world value

### 3.3 No Cloud Dependencies in V1
- No API calls to OpenAI, Anthropic, Google, AWS, Azure, or any cloud AI service
- No cloud storage, no cloud authentication, no cloud analytics
- No Firebase, no Crashlytics, no Google Analytics, no any-cloud-SDK
- If an approach requires a cloud service, it is the wrong approach for V1

### 3.4 No Analytics or Tracking Code
- Do not add usage tracking, event logging, crash reporters, or analytics libraries
- Do not add device ID collection, session tracking, or behavioural logging
- Do not add "optional" telemetry that is on by default
- All logging must be local-only debug logging, stripped from production builds

### 3.5 All Learner Data Must Remain Local
- Learner profile data stays on the device — never transmitted
- Do not design sync features that send learner data anywhere
- If a feature requires transmitting learner data, it is out of scope for V1

---

## 4. Architecture Decisions Are Already Made

Do not re-open these decisions without explicit instruction:

| Decision | Reference | What It Means |
|----------|-----------|---------------|
| Phone-first | ADR-001 | The phone is always the primary compute surface |
| Offline-first | ADR-002 | All core features work with no connectivity |
| Edge as accelerator | ADR-003 | School node is optional; phone works without it |
| Retrieval-first | vision.md | Model explains retrieved content — does not invent |
| GGUF/ONNX models | constraints.md | Quantized models only; no PyTorch runtime in production |

If a task seems to require revisiting one of these decisions, create an ADR proposal — do not silently implement an alternative.

---

## 5. Code Quality Expectations

- **Prefer simple, maintainable code** over clever optimisations
- **Comment only where intent is non-obvious** — do not over-comment
- **Every feature must have clear offline behaviour** — document what happens when connectivity is absent
- **Minimal dependencies** — justify every new library before adding it
- **Battery and memory conscious** — no background processing, no unnecessary allocations
- **Open source only** — all dependencies must be open source with compatible licences

See [`docs/development/coding-principles.md`](./coding-principles.md) for the full list.

---

## 6. Content and Model Grounding

- LLM responses for curriculum questions must be grounded in retrieved content pack data
- The model must not answer from parametric memory alone for educational content
- Prompt templates must enforce retrieval-grounded generation
- If no relevant content is found, the system must say so — not hallucinate
- Do not create or modify content pack data — content authoring is a separate process

---

## 7. EJS Journey System

This project uses the EJS (Emergent Journey System) for session documentation.

- If you complete a significant session of work, document it in `ejs-docs/journey/`
- Use the journey template at `ejs-docs/journey/_templates/journey-template.md`
- If your session involves a significant architectural decision, create an ADR in `docs/adr/`
- Use `docs/adr/ADR-000-template.md` as the ADR template

---

## 8. When You Are Uncertain

If you are uncertain about:
- Whether a feature is in V1 scope → **check vision.md Section 10 and flag if unclear**
- Whether an approach is offline-safe → **assume it must be and design accordingly**
- Whether a library is acceptable → **check for cloud dependencies and licence compatibility**
- Whether a design decision conflicts with an ADR → **flag the conflict, do not override silently**
- Whether learner data is involved → **assume it is sensitive and keep it local**

When in doubt, do less and ask. Implementing the wrong thing confidently is worse than flagging uncertainty.

---

## 9. Related Documents

- [Coding Principles](./coding-principles.md)
- [V1 Backlog](./backlog-v1.md)
- [Product Vision](../product/vision.md)
- [Constraints](../product/constraints.md)
- [ADR Index](../adr/)
