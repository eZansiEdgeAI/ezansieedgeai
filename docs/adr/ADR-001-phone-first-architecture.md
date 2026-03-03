# ADR-001: Phone-First Architecture

## Status
accepted

## Context
eZansiEdgeAI is designed for underserved South African schools. When evaluating where primary compute should live, two options were considered:

**Option A — Device-First (Classroom Nodes)**  
Deploy dedicated compute hardware (e.g., Raspberry Pi, mini PC) as the primary AI processing unit in each classroom. Learner phones act as thin clients.

**Option B — Phone-First**  
Treat the learner's phone as the primary compute surface. Dedicated hardware is optional and supplementary only.

Key contextual factors:
- Raspberry Pi and similar hardware has fluctuating availability and supply chain risk
- Physical hardware in schools is subject to theft, damage, and power failure
- Hardware maintenance requires on-site technical support — unavailable in most target schools
- Scaling hardware per classroom per school is operationally expensive
- Learners already own or have access to an Android phone
- Phones are already charged, already trusted, and already familiar to learners
- A phone-only approach requires zero additional hardware procurement

## Decision
The learner phone is the primary compute surface for all core learning functionality.

All inference (LLM, embeddings), content retrieval, and learner profile management runs on the phone. School edge devices and community hub nodes are optional capability accelerators — they enhance the experience but are never required for core learning to function.

## Rationale
- Phones are already present in the target environment — no procurement barrier
- Phone-first eliminates all hardware deployment, maintenance, and theft risk
- Every learner carries their compute surface — learning continues at home, in transit, anywhere
- Reduces project dependencies: no hardware supply chain, no physical installation
- The approach is more equitable: capability scales with the phone the learner has, not with what the school can afford

Rejected alternative: Device-first classroom nodes were rejected because they introduce procurement cost, physical security risk, maintenance complexity, and a single point of failure for an entire classroom.

## Consequences

### Positive
- Zero hardware cost for core learning functionality
- Learning continues offline at home, in transit, and during load shedding
- No hardware procurement, shipping, or installation process
- Resilient by design — no shared hardware single point of failure
- Learner owns their compute surface — improves sense of agency

### Negative / Trade-offs
- Limited compute per device — models must be aggressively quantized
- Performance varies across the installed phone base — some learners will have faster experiences than others
- Storage is shared with other apps — content packs compete for limited space
- Battery impact of on-device inference must be carefully managed
- No centralised model upgrade path — model updates must reach individual devices
