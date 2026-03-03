# eZansiEdgeAI: Product Constraints

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Architects, Product Owners

---

## 1. Purpose

These constraints are not limitations to work around — they are the design specification. Every feature decision must be validated against this list. If a design choice conflicts with a constraint, the design must change, not the constraint.

---

## 2. Hardware Constraints

### 2.1 Target Device
- Android 10 or higher
- ~3 GB RAM (minimum viable); 4–6 GB target
- ARM64 CPU; NPU/GPU acceleration is optional, not assumed
- Limited available storage (shared with other apps, media, OS)
- Battery sensitivity: thermal limits under sustained CPU load

### 2.2 Implications for Design
- **No large models.** Models must be quantized to fit within ~1.5–2 GB RAM.
- **No background inference.** LLM runs only on explicit user query.
- **No memory leaks.** All inference sessions must be cleaned up promptly.
- **Minimal dependencies.** Each library added increases APK size and RAM footprint.
- **Storage budget matters.** Content packs + models + app must fit within ~3–4 GB total.

### 2.3 Model Format Requirements
- GGUF (for llama.cpp-based runtimes) — preferred for phone
- ONNX (for ONNX Runtime Mobile) — preferred for cross-platform and embeddings
- No PyTorch runtime in production app — too heavy
- No model fine-tuning on device — inference only

---

## 3. Connectivity Constraints

### 3.1 Connectivity Realities
- Load shedding is frequent and unpredictable (up to 8+ hours/day in some areas)
- Learners may have no home internet connection
- School internet connections are often intermittent and slow
- Mobile data is expensive — learners cannot be expected to use data for the app
- WiFi is available at some schools — but cannot be assumed

### 3.2 Implications for Design
- **Full offline operation is mandatory after installation.**
- **No runtime API calls** to any external service — ever — in core learning flow.
- **No CDN dependencies** for content delivery.
- **Pack updates must work over LAN** — never require internet at the phone level.
- **App startup must not require connectivity** — no splash-screen "checking for updates" blocks.
- **Content must be pre-bundled** — not streamed or downloaded at query time.

---

## 4. Deployment Constraints

### 4.1 School Environment Reality
- No dedicated school IT support in many target schools
- No school cloud accounts or email addresses
- No school payment methods or subscription capability
- Physical security risks for shared hardware
- No guarantee of electricity during school hours (load shedding schedules vary)

### 4.2 Implications for Design
- **Installation must be a single APK** — no multi-step setup wizards.
- **No account creation required** — app works immediately after install.
- **No subscription or payment gate** — fully free to operate.
- **Edge node software must auto-start** on power restoration (no manual restart).
- **All configuration must have safe defaults** — zero-config out of the box.
- **Updates must not break existing functionality** — no force-update gates.

---

## 5. Adoption Constraints

### 5.1 User Reality
- Learners are Grade 6 students — must be immediately intuitive
- Teachers have limited digital literacy — install process must be trivial
- Any friction (setup, registration, login, loading time) = abandonment
- Privacy concerns are real — tracking fears reduce trust
- Battery anxiety is real — heavy battery usage = uninstall

### 5.2 Implications for Design
- **First run must reach "useful" in under 60 seconds.**
- **No login, no registration, no email** required at any point.
- **UI must be simple** — optimise for clarity, not feature richness.
- **Explain what the app is doing** — no mysterious spinners or long silences.
- **Battery usage must be disclosed** — inference cost shown or minimised.
- **Privacy must be visible** — learner can see what is stored and delete it.
- **No dark patterns** — no nudges to share data, no optional "analytics" opt-ins.

---

## 6. Model and Content Constraints

### 6.1 Model Selection Criteria
- Must run on CPU without GPU acceleration
- Must fit within ~1.5 GB RAM for LLM; ~50–100 MB for embedding model
- Must produce coherent, curriculum-appropriate explanations in English
- GGUF quantization levels: Q4_K_M or Q5_K_M preferred (balance of quality vs size)
- Total model storage footprint: < 2 GB preferred, hard max 3 GB

### 6.2 Content Pack Constraints
- Each pack must be self-contained — no cross-pack dependencies in V1
- Pack size target: < 200 MB per term pack (text + embeddings)
- Packs must be versioned and replaceable without reinstalling the app
- Content must be CAPS-aligned — accuracy is non-negotiable
- Content must be reviewed before packaging — model does not generate curriculum

### 6.3 Scope Discipline
- V1 is Grade 6 Mathematics only — no scope creep
- Additional subjects / grades are post-V1 work
- The content pack format must support multi-subject in future — design for extensibility

---

## 7. Constraint Validation Checklist

Before shipping any feature, validate against:

| Constraint | Question to ask |
|------------|----------------|
| Hardware | Does this work on 3GB RAM Android 10? |
| Offline | Does this work with no internet, ever? |
| Storage | Does this fit within our storage budget? |
| Battery | Does this avoid unnecessary background CPU use? |
| Deployment | Can a non-technical person set this up? |
| Adoption | Can a Grade 6 learner use this without a manual? |
| Privacy | Does any learner data leave the device? |
| Cost | Does this cost anything to operate? |

---

## 8. Related Documents

- [Product Vision](./vision.md)
- [Success Metrics](./success-metrics.md)
- [Phone Architecture](../architecture/phone-architecture.md)
- [ADR-002 — Offline First Design](../adr/ADR-002-offline-first-design.md)
