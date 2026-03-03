# eZansiEdgeAI: Phone Architecture

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Android Developers

---

## 1. Purpose

The learner phone is the **primary compute surface** for eZansiEdgeAI. All core functionality — question answering, content retrieval, explanation generation, and learner preference management — runs entirely on-device. No network connection is required for learning to work.

This document details each layer of the phone stack.

---

## 2. Phone Stack Overview

```
┌─────────────────────────────────────────────┐
│                  APP LAYER                  │
│  Learning UI  │  Chat Interface  │ Voice UI  │
│  Personal Learning Profile                  │
│  Local Content Library                      │
├─────────────────────────────────────────────┤
│                  AI LAYER                   │
│  Quantized Small LLM (GGUF / ONNX)          │
│  Embeddings (tiny model)                    │
│  Prompt Templates                           │
├─────────────────────────────────────────────┤
│                 DATA LAYER                  │
│  Local Vector DB                            │
│  Encrypted Learner Profile                  │
│  Offline Content Packs                      │
├─────────────────────────────────────────────┤
│               HARDWARE LAYER                │
│  CPU / NPU (if available)                   │
│  3–6 GB RAM target                          │
│  Offline Storage                            │
└─────────────────────────────────────────────┘
```

---

## 3. App Layer

The App Layer is the user-facing surface. It must be simple, fast, and usable without training.

### 3.1 Learning UI
- Primary screen for interacting with curriculum content
- Displays retrieved content, worked examples, and explanations
- Supports step-by-step breakdown of problems
- Designed for small screens; touch-first layout

### 3.2 Chat Interface
- Text-based question input (V1 primary interface)
- Conversational answer display
- Follows a question → retrieve → explain → example pattern
- Keeps session history locally for context continuity

### 3.3 Voice UI
- Planned for post-V1 (requires STT, ideally from school node)
- Voice input captured and sent to local or LAN STT
- Voice output via on-device TTS (basic) or school node TTS
- Must degrade gracefully to text-only if unavailable

### 3.4 Personal Learning Profile
- Stores learner preferences locally only
- Captures: explanation style, reading level, example type, pace preference
- Editable by the learner at any time
- Used to shape prompt construction in the AI Layer
- Never transmitted off-device in V1

### 3.5 Local Content Library
- Lists installed content packs (e.g., "Grade 6 Maths — Term 1")
- Shows pack version and last-updated date
- Allows manual pack import from local storage or WiFi sync
- Manages storage allocation across packs

---

## 4. AI Layer

The AI Layer runs entirely on-device. All inference is local. No API calls to external services.

### 4.1 Quantized Small LLM (GGUF / ONNX)
- Small language model, quantized to reduce memory footprint
- Format: GGUF (llama.cpp runtime) or ONNX (ONNX Runtime Mobile)
- Role: generate curriculum-grounded explanations from retrieved content
- **Does not invent knowledge** — always grounded via retrieved context
- Target: fits within ~1.5–2GB RAM allocation
- Runs on CPU; uses NPU/GPU acceleration if available on device

### 4.2 Embeddings (Tiny Model)
- Lightweight sentence embedding model
- Converts learner questions into vectors for similarity search
- Must run fast (< 200ms per query target)
- Format: ONNX preferred for cross-platform compatibility
- Target: < 100MB storage footprint

### 4.3 Prompt Templates
- Pre-built prompt structures for common query types:
  - Concept explanation
  - Worked example request
  - Step-by-step breakdown
  - Definition lookup
- Templates incorporate learner profile preferences at runtime
- Curriculum-grounding context inserted from Data Layer retrieval
- Templates versioned alongside content packs

---

## 5. Data Layer

The Data Layer persists all content and learner data locally on the device.

### 5.1 Local Vector DB
- Stores embeddings for all content in installed packs
- Enables fast semantic similarity search for retrieval
- Lightweight embedded DB (e.g., SQLite-backed or FAISS-style flat index)
- Rebuilt on pack install; incremental updates supported

### 5.2 Encrypted Learner Profile
- Stores personal learning preferences
- Encrypted at rest using device-level key
- Schema: preference signals only — no performance scores, no behaviour logs
- Exportable by learner in plain text
- Deleted on learner request (no remote backup)

### 5.3 Offline Content Packs
- Versioned bundles of curriculum content
- Pack structure:
  - Raw content chunks (text)
  - Pre-computed embeddings
  - Pack metadata (subject, grade, term, version, language)
  - Optional: worked examples, diagrams (future)
- Distributed via school node WiFi or manual sideload
- Stored in device internal storage (no SD card dependency in V1)

---

## 6. Hardware Layer

### 6.1 Target Hardware Specification

| Property | Minimum | Target |
|----------|---------|--------|
| OS | Android 10 | Android 12+ |
| RAM | 3 GB | 4–6 GB |
| Storage free | 2 GB | 4+ GB |
| CPU | ARM64 | ARM64 with NPU preferred |
| GPU / NPU | Not required | Optional acceleration |
| Battery | 3000 mAh | 4000+ mAh preferred |

### 6.2 Performance Targets

| Operation | Target Latency |
|-----------|----------------|
| Embedding a question | < 200ms |
| Vector retrieval | < 100ms |
| LLM explanation generation | < 8 seconds |
| App launch to ready | < 3 seconds |

### 6.3 Battery Considerations
- LLM inference is the primary battery cost
- Inference runs only on explicit user query — no background processing
- Model loaded once per session, not per query
- Background sync (pack updates) runs only when plugged in or on WiFi with user consent

---

## 7. Related Documents

- [System Overview](./system-overview.md)
- [Edge Device Architecture](./edge-device-architecture.md)
- [Constraints](../product/constraints.md)
- [ADR-001 — Phone-First Architecture](../adr/ADR-001-phone-first-architecture.md)
