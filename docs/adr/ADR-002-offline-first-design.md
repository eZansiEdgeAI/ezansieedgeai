# ADR-002: Offline-First Design

## Status
accepted

## Context
The target deployment environment for eZansiEdgeAI includes schools and homes where internet connectivity cannot be assumed. Key realities:

- **Load shedding:** South Africa experiences scheduled power cuts (load shedding) lasting 2–8+ hours per day in many regions. During outages, routers and school internet connections go down.
- **Expensive mobile data:** Learners use prepaid mobile data carefully. An app that consumes data for normal operation creates a direct cost barrier.
- **Intermittent or absent school internet:** Many target schools have slow or unreliable internet connections. Rural schools may have none.
- **Home connectivity:** The majority of learners in the target group have no home broadband. Mobile data is their only connectivity option.

Two approaches were evaluated:

**Option A — Online-Assisted (Cloud Dependency)**  
Core features work best online; degraded or non-functional offline.

**Option B — Offline-First**  
All core features work fully offline. Online connectivity is used opportunistically for enhancement (pack updates, model updates) but is never required.

## Decision
The system must work fully offline after installation. Once the app and at least one content pack are installed, a learner must be able to ask questions and receive grounded explanations with zero network activity.

No core learning feature may require an internet connection or LAN connection at runtime. Connectivity is used only for:
- Initial app download / installation
- Content pack updates (opportunistic, over LAN or internet)
- App and model updates (opportunistic, over LAN or internet)

## Rationale
- The primary users — learners — cannot be expected to have reliable internet
- Load shedding eliminates connectivity for hours at a time even in well-connected schools
- Mobile data cost is a direct barrier to access if the app requires online operation
- Offline-first aligns with the core mission: no learner locked out by circumstances
- Retrieval-first architecture (local content packs + local embeddings) makes offline LLM grounding viable without cloud APIs

Rejected alternative: Online-assisted design was rejected because it would make the system unusable for the majority of the target audience the majority of the time.

## Consequences

### Positive
- System works in all environments — load shedding, no internet, remote areas
- No mobile data cost for learning — removes a direct cost barrier
- Privacy benefit: no data transmitted during learning sessions
- Resilient by design — no external dependency can break core functionality
- Works at home, at school, in transit — wherever the learner is

### Negative / Trade-offs
- Content update distribution is more complex — cannot push updates directly to devices
- Model updates must be distributed via LAN or manual sideload
- Content accuracy depends on the installed pack version — stale packs are a risk
- Initial installation requires connectivity or physical distribution (APK + pack bundle)
- No real-time content from the internet — cannot answer questions about today's news or events (intentional for V1)
