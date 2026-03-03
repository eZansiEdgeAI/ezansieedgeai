# eZansiEdgeAI: System Overview

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Technical Partners

---

## 1. Purpose

This document provides a high-level overview of the eZansiEdgeAI system architecture. It describes the two-tier design, how data flows between components, and the key decisions that shaped the architecture.

---

## 2. Architecture Summary

eZansiEdgeAI is a **two-tier, offline-first system**:

| Tier | Component | Role |
|------|-----------|------|
| **Primary** | Learner Phone | All core learning happens here — always |
| **Optional** | School Edge Node | Capability accelerator — never a dependency |

The phone is the brain. The school node is a booster.  
If the node is unavailable, learning continues uninterrupted.

---

## 3. System Diagram

```
┌──────────────────────────────────────────────────┐
│                  LEARNER PHONE                   │
│                                                  │
│  ┌─────────────┐  ┌──────────────┐               │
│  │  App Layer  │  │   AI Layer   │               │
│  │  Learning UI│  │  Quantized   │               │
│  │  Chat UI    │  │  LLM (GGUF)  │               │
│  │  Voice UI   │  │  Embeddings  │               │
│  │  Profile    │  │  Prompt Tmpl │               │
│  └──────┬──────┘  └──────┬───────┘               │
│         └────────┬────────┘                      │
│              ┌───▼──────────┐                    │
│              │  Data Layer  │                    │
│              │  Vector DB   │                    │
│              │  Learner     │                    │
│              │  Profile     │                    │
│              │  Content     │                    │
│              │  Packs       │                    │
│              └──────────────┘                    │
└────────────────────┬─────────────────────────────┘
                     │ WiFi (LAN only, optional)
                     │
┌────────────────────▼─────────────────────────────┐
│             SCHOOL EDGE NODE (optional)          │
│                                                  │
│  ┌───────────────────┐  ┌─────────────────────┐  │
│  │ WiFi Service Layer│  │    AI Services      │  │
│  │ Local API Gateway │  │    Shared STT       │  │
│  │ Content Distrib.  │  │    Shared TTS       │  │
│  │ Update Server     │  │    Optional Model   │  │
│  └───────────────────┘  └─────────────────────┘  │
│                                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │              Data Services                  │ │
│  │   Shared Content Cache  │  School KB        │ │
│  └─────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────┘
```

---

## 4. Data Flow

### 4.1 Offline Query Flow (Phone Only — always available)

```
Learner Question
    → App Layer (Chat / Voice UI)
    → AI Layer: embed question (tiny model)
    → Data Layer: vector search over local Content Pack
    → AI Layer: LLM generates grounded explanation from retrieved content
    → App Layer: display response
    → Data Layer: update Learner Profile (local only)
```

### 4.2 Content Update Flow (When School Node is Present)

```
School Node broadcasts availability on LAN
    → Phone discovers node via local WiFi
    → Phone requests content pack manifest
    → Phone downloads updated / new content packs over LAN
    → No internet required at any point
```

### 4.3 Voice-Assisted Flow (When School Node is Present)

```
Learner speaks question
    → App captures audio
    → Sends to School Node STT service (LAN)
    → Receives transcript
    → Continues as standard Offline Query Flow
```

---

## 5. Key Design Decisions

| Decision | Rationale | ADR |
|----------|-----------|-----|
| Phone as primary compute surface | Phones are already owned, charged, and trusted | [ADR-001](../adr/ADR-001-phone-first-architecture.md) |
| Fully offline after installation | Load shedding, expensive data, no connectivity guarantees | [ADR-002](../adr/ADR-002-offline-first-design.md) |
| School node as accelerator, not brain | Availability of school infrastructure cannot be assumed | [ADR-003](../adr/ADR-003-edge-device-as-accelerator.md) |
| Retrieval-first over model memory | Reduces hallucination, enables curriculum grounding | docs/product/vision.md |
| Quantized small models (GGUF/ONNX) | Fits within ~3GB RAM, runs on CPU without GPU | docs/product/constraints.md |
| No cloud dependency in V1 | Zero cost to operate, works in any environment | docs/product/constraints.md |
| Local-only learner data | Privacy by design, no surveillance | docs/product/vision.md |

---

## 6. V1 Scope Boundary

V1 is deliberately narrow:

- **Subject:** Grade 6 Mathematics only
- **Curriculum:** CAPS aligned
- **Interface:** Text first
- **Connectivity:** Offline only required
- **Platform:** Android 10+

Scope will expand only after V1 demonstrates real-world value.

---

## 7. Related Documents

- [Phone Architecture](./phone-architecture.md)
- [Edge Device Architecture](./edge-device-architecture.md)
- [Deployment Modes](./deployment-modes.md)
- [Product Vision](../product/vision.md)
- [Constraints](../product/constraints.md)
