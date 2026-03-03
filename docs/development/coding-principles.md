# eZansiEdgeAI: Coding Principles

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** All Contributors

---

## 1. Purpose

These principles guide all code written for eZansiEdgeAI. They are not preferences — they are requirements derived directly from the project's constraints and mission. When in doubt, return to this list.

---

## 2. Offline First in Every Feature Decision

- Every feature must work without any network connection
- Network calls are permitted only for optional enhancements (content sync, model updates)
- A feature that degrades or breaks when offline is not complete
- Test offline behaviour explicitly — do not assume it works

**Ask before every feature:** "Does this work with no internet, ever?"

---

## 3. Minimal Dependencies

- Prefer standard library or bundled implementations over third-party libraries
- Every dependency added is additional APK size, RAM footprint, and maintenance burden
- Evaluate every new library against: Could we implement the needed function ourselves in < 100 lines?
- No large framework dependencies unless they provide irreplaceable value
- All dependencies must be open source with compatible licences

**Ask before adding a dependency:** "Is this truly necessary, and does it have a compatible open source licence?"

---

## 4. Battery and Memory Conscious Code

- LLM inference runs only when explicitly triggered by a user action — never in background
- Load models once per session; do not reload per query
- Release model memory when the app is backgrounded for more than 5 minutes
- Avoid wake locks and background CPU usage
- Profile memory usage on minimum-spec devices (3GB RAM Android 10)
- Avoid memory leaks — every inference session must be cleaned up

**Ask before every long-running operation:** "Does this run in the background? Should it?"

---

## 5. No Telemetry or Data Phoning Home

- Zero analytics calls, crash reporters, or tracking SDKs in the production build
- No usage events sent anywhere, ever
- No third-party analytics libraries (Google Analytics, Firebase, Amplitude, etc.)
- Crash logging is local only — debug builds may log to device; production builds do not transmit
- If a library includes built-in telemetry, it must be disabled or the library must be replaced

**Rationale:** Learner trust depends on the app doing what it says — nothing more. Telemetry in an app for vulnerable learners violates that trust.

---

## 6. Content Grounding — The Model Explains, It Does Not Invent

- All LLM responses must be grounded in retrieved content from the local content pack
- The model must not answer from its parametric memory alone for curriculum questions
- Every query follows the pattern: retrieve relevant content → insert into prompt → generate explanation from that content
- If no relevant content is found in the pack, the response must say so — not hallucinate an answer
- Prompt templates must enforce content grounding — this is an architectural constraint, not a best-effort behaviour

**Rationale:** Content accuracy is essential for educational trust. A wrong answer is worse than no answer.

---

## 7. Privacy by Design — Learner Data Stays on Device

- All learner data (preferences, session context, history) is stored locally only
- No learner data is transmitted to any server — school node, cloud, or otherwise
- Learner profile data must be encrypted at rest using device-level keys
- Learner must be able to view all stored data in plain language
- Learner must be able to delete all stored data from within the app
- No device identifiers (IMEI, advertising ID, etc.) are collected or stored

**Rationale:** Learners in this context are minors. Their data must be protected unconditionally.

---

## 8. Open Source Stack Only

- All runtime dependencies must be open source with licences compatible with this project
- No proprietary SDKs, closed-source models, or commercial runtimes in the core stack
- Model weights must be available under a licence that permits distribution with the app
- If a component cannot be open-sourced, it cannot be part of the core system

**Rationale:** Zero cost to schools means zero licensing cost. Open source is not optional — it is a strategic requirement.

---

## 9. Simple and Maintainable Over Clever

- Write code that a new contributor can understand without deep context
- Avoid over-engineering: solve the problem in front of you, not the hypothetical future problem
- Leave clear comments only where the code's intent is genuinely non-obvious
- Prefer explicit over implicit
- If a solution requires a long explanation to justify, consider whether a simpler solution exists

---

## 10. Related Documents

- [AI Agent Instructions](./ai-agent-instructions.md)
- [Product Constraints](../product/constraints.md)
- [ADR-002 — Offline First Design](../adr/ADR-002-offline-first-design.md)
- [Product Vision](../product/vision.md)
