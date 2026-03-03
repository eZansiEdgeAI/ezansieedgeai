# eZansiEdgeAI: V1 Backlog

**Status:** Active  
**Last Updated:** 2026-02  
**Audience:** Contributors, Product Owners

---

## 1. Purpose

This backlog defines the work required to ship V1 of eZansiEdgeAI. It is structured as four phases across approximately 13 weeks. Each phase has clear deliverables and explicit success criteria.

**V1 Scope Reminder:**
- Subject: Grade 6 Mathematics only
- Curriculum: CAPS aligned
- Interface: Text first
- Connectivity: Offline only required
- Platform: Android 10+

Anything not listed here is out of scope for V1.

---

## 2. Phase 0 — Feasibility Spikes (Weeks 1–2)

**Goal:** Validate that the core technical approach is viable on target hardware before building the full system.

### Spikes

#### SPIKE-001: On-Device Inference Viability
- Select 2–3 candidate quantized models (GGUF Q4/Q5)
- Test inference on minimum spec device (Android 10, ~3GB RAM)
- Measure: inference time, RAM usage, battery draw per query, thermal behaviour
- Decision gate: is a usable response latency achievable (< 8s target)?
- Document findings in `ejs-docs/journey/`

#### SPIKE-002: Local Embedding + Retrieval
- Select candidate embedding model (ONNX, < 100MB)
- Build minimal local vector store prototype (SQLite or flat FAISS)
- Measure: embedding time per chunk, retrieval time per query, storage per 1000 chunks
- Decision gate: is retrieval fast enough to be part of a fluid query flow (< 300ms)?

#### SPIKE-003: Storage Footprint Validation
- Profile total storage budget: app + model + embedding model + 1 content pack
- Test on device with 3GB RAM and 16GB total storage (real-world constraint)
- Decision gate: can we fit within ~3–4GB total footprint?
- Document recommended model and pack size targets

### Phase 0 Exit Criteria
- [ ] All three spikes completed and documented
- [ ] Model candidate selected for V1
- [ ] Embedding model candidate selected for V1
- [ ] Storage budget confirmed and documented in constraints.md
- [ ] No blocking technical risks identified (or risks documented with mitigation plan)

---

## 3. Phase 1 — Offline Learning Loop (Weeks 3–6)

**Goal:** Build the minimum working learning loop — a learner can ask a question and get a grounded explanation, fully offline.

### Features

#### FEAT-101: Basic Android App Shell
- Single-screen chat interface (text in, text out)
- No login, no onboarding, immediate access on first launch
- Offline-first: app must start without connectivity
- Target: Android 10+, ARM64

#### FEAT-102: Offline Content Pack Loading
- App reads a content pack from device storage
- Pack format: versioned JSON/binary bundle (text chunks + metadata)
- Pack metadata visible in app (subject, grade, term, version)
- Manual pack install via file picker (no network required)

#### FEAT-103: Embedding Pipeline (On-Device)
- On-device embedding of learner question using ONNX model
- Pack chunks embedded at install time and stored in local vector index
- Vector similarity search on query to retrieve top-k relevant chunks

#### FEAT-104: Retrieval + Explanation Pipeline
- Retrieved chunks injected into prompt template
- LLM generates explanation grounded in retrieved content
- Response displayed in chat interface
- Handles case where no relevant content found gracefully

#### FEAT-105: Basic Learner Preference Profile (Local)
- Learner can set: explanation style (simple / detailed), example preference (yes/no)
- Preferences stored locally, encrypted at rest
- Preferences shape prompt template construction
- Learner can edit or delete preferences

### Phase 1 Exit Criteria
- [ ] End-to-end query flow working offline on minimum spec device
- [ ] Content pack loads successfully from local storage
- [ ] Responses are grounded in pack content (spot-checked manually)
- [ ] App starts in < 3 seconds
- [ ] Query-to-response in < 8 seconds on minimum spec device
- [ ] No crashes during 10-minute continuous use session

---

## 4. Phase 2 — Content + Personalisation (Weeks 7–10)

**Goal:** Deliver real curriculum content and a working personalisation engine.

### Features

#### FEAT-201: Learner Preference Engine (Enhanced)
- Expand preference signals: reading level, pace, language preference
- Preferences applied dynamically to prompt templates
- Preference adjustment available inline during a session
- Preferences persist between sessions

#### FEAT-202: Content Pack Builder Tooling
- CLI tool to build a content pack from raw source material
- Input: CAPS-aligned text files (markdown or plain text)
- Output: versioned pack bundle (text chunks + pre-computed embeddings + metadata)
- Pack signing for integrity verification
- Located in `tools/content-pack-builder/`

#### FEAT-203: Grade 6 CAPS Mathematics Pack — Term 1
- First real content pack: Grade 6 Maths, Term 1, CAPS aligned
- Content reviewed by at least one subject matter expert
- Pack built using FEAT-202 tooling
- Covers all Term 1 topics (numbers, operations, patterns — per CAPS)
- Includes worked examples per topic

#### FEAT-204: Worked Example Display
- App displays worked examples as part of explanation response
- Step-by-step breakdown format
- Learner can request additional examples ("show me another example")

#### FEAT-205: Session Context (Short-Term Memory)
- App maintains context of current session (last 3–5 exchanges)
- Context injected into prompt for follow-up questions
- Context cleared when learner starts a new topic
- Session history stored locally; not persisted between app restarts in V1

### Phase 2 Exit Criteria
- [ ] Grade 6 Term 1 CAPS pack complete and content-reviewed
- [ ] Pack builder tool documented and tested
- [ ] Personalisation preferences demonstrably affect response quality
- [ ] Worked examples are clear and accurate
- [ ] Session context enables natural follow-up questions

---

## 5. Phase 3 — School Node + Hardening (Weeks 11–13)

**Goal:** Add school edge node capability and harden the app for real-world deployment.

### Features

#### FEAT-301: LAN Node Discovery
- App broadcasts LAN probe on startup
- Edge node responds with available services manifest
- Phone selects services to use based on availability
- Timeout and graceful fallback to offline-only mode (< 2 seconds)

#### FEAT-302: Content Pack Sync Over WiFi
- Phone requests pack manifest from edge node
- Phone downloads updated or new packs over LAN
- Differential updates supported (download only changed chunks)
- Sync is background and non-blocking to learning

#### FEAT-303: Edge Node — Content Distribution Service
- Edge node software: content distribution server
- Hosts pack repository; responds to phone manifest and download requests
- Auto-starts on system boot; recovers after power restoration
- Minimal configuration required

#### FEAT-304: Battery and Reliability Testing
- Structured test on minimum spec device: 30-minute continuous use session
- Battery consumption measured and documented
- Memory usage profiled across session
- Crash testing: force-close during inference, low storage, low memory conditions
- Results documented; any critical issues resolved before release

#### FEAT-305: Installation and Deployment Guide
- Step-by-step guide for teacher-level installation (APK + content pack)
- Step-by-step guide for edge node setup (for school admin / NGO)
- Tested with non-technical users
- Available as a PDF for offline distribution

### Phase 3 Exit Criteria
- [ ] LAN discovery works reliably (node present and absent cases)
- [ ] Pack sync completes successfully over LAN
- [ ] Edge node auto-recovers after simulated power cut
- [ ] 30-minute session battery test passed on minimum spec device
- [ ] No blocking bugs identified in reliability testing
- [ ] Installation guide tested with at least one non-technical tester
- [ ] All V1 success metrics (docs/product/success-metrics.md) verified

---

## 6. Out of Scope for V1

The following are explicitly deferred to post-V1:

- Voice input / Speech-to-Text interface
- Voice output / Text-to-Speech
- Teacher dashboard
- Multi-subject support (any subject other than Grade 6 Maths)
- Multi-grade support
- Cloud integration of any kind
- Learner performance tracking or analytics
- Community content pack authoring portal
- Language support beyond English (Afrikaans and others are post-V1)
- Advanced agent orchestration
- Offline multiplayer learning features

---

## 7. Related Documents

- [Product Vision](../product/vision.md)
- [Constraints](../product/constraints.md)
- [Success Metrics](../product/success-metrics.md)
- [Coding Principles](./coding-principles.md)
- [AI Agent Instructions](./ai-agent-instructions.md)
