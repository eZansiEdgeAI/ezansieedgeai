# ADR-001: Phone-First Architecture

* **Status:** Accepted
* **Date:** 2026-02-16
* **Decision Makers:** Project Team
* **Technical Story:** Strategic direction reset based on real-world constraints analysis

## Context and Problem Statement

eZansiEdgeAI aims to provide AI-powered learning support to underserved learners in South Africa. We need to decide what the primary compute platform should be: classroom-based devices (like Raspberry Pi), cloud-based services, or learner-owned phones.

The key question: **What hardware platform should we build for first, given the constraints of our target users?**

## Decision Drivers

* **Device Ownership:** Learners and families increasingly own smartphones, even in underserved communities
* **Infrastructure Reality:** Schools often lack reliable power, internet, and IT support
* **Maintenance Burden:** Classroom devices require ongoing maintenance, replacement, and security
* **Cost Distribution:** Phone-first puts compute costs on devices already owned rather than requiring new purchases
* **Trust and Privacy:** Learners trust their personal devices more than shared school equipment
* **Connectivity:** Phones have built-in offline capability and optional mobile data fallback
* **Scalability:** Phone-first scales with device ownership, not school infrastructure deployment

## Considered Options

1. **Classroom Raspberry Pi Devices** (original plan)
2. **Cloud-First Architecture**
3. **Phone-First Architecture** (with optional school enhancement)

## Decision Outcome

**Chosen option:** "Phone-First Architecture"

The learner's personal Android phone is the primary compute platform. All core functionality (question answering, content retrieval, AI inference) happens on the phone. School-based edge devices are optional enhancements, not dependencies.

### Reasoning

Research into deployment realities revealed that:

1. **Phones are already there:** Most learners (even in underserved communities) have access to a smartphone, either personal or family-shared
2. **Infrastructure is unreliable:** Load shedding, theft, lack of IT support make school-based hardware deployments fragile
3. **Privacy and trust:** Learners are more comfortable using their own devices than shared school equipment
4. **Lower barrier to adoption:** No school infrastructure required means faster deployment and broader reach
5. **Better alignment with real usage:** Learners do homework at home, not just at school

### Positive Consequences

* **Faster time to deployment:** No need to procure, ship, and set up school hardware first
* **Broader reach:** Can serve learners whose schools have no infrastructure at all
* **Lower operational cost:** No hardware replacement, maintenance, or security costs
* **Better privacy:** Data stays on learner's device, not shared equipment
* **More usage opportunities:** Available wherever learner has their phone (home, library, community center)
* **Graceful enhancement:** Can add school nodes later without breaking existing functionality

### Negative Consequences

* **Device heterogeneity:** Must support wide range of phone capabilities (low-end to mid-range)
* **Limited compute:** Constrained to what can run on 3GB RAM Android devices
* **Storage constraints:** Must fit app + content + models in limited phone storage
* **Battery sensitivity:** Must be very careful with battery usage or app will be uninstalled
* **No shared services:** STT/TTS services delayed to future phase when school nodes added

## Pros and Cons of the Options

### Classroom Raspberry Pi Devices (Original Plan)

* **Good:** Controlled hardware environment, known specifications
* **Good:** Can run larger models with more compute/RAM
* **Good:** Single installation point in classroom
* **Bad:** Requires power (load shedding problem)
* **Bad:** Requires maintenance and IT support
* **Bad:** Theft and physical security risk
* **Bad:** Only available during school hours
* **Bad:** High upfront cost and ongoing operational burden
* **Bad:** Scales poorly (need device per classroom)

### Cloud-First Architecture

* **Good:** Powerful compute, latest models
* **Good:** Easy to update and maintain
* **Good:** Centralized monitoring and analytics
* **Bad:** Requires internet connectivity (excludes many target users)
* **Bad:** Ongoing costs (subscription or data)
* **Bad:** Privacy concerns (data leaves device)
* **Bad:** Not aligned with "offline-first" mission
* **Bad:** Reinforces digital divide rather than addressing it

### Phone-First Architecture (Chosen)

* **Good:** Uses hardware learners already own
* **Good:** Works offline completely
* **Good:** Privacy-preserving (data stays local)
* **Good:** Available wherever learner is
* **Good:** No school infrastructure dependency
* **Good:** Lower barrier to adoption
* **Good:** Scales with device ownership, not infrastructure
* **Bad:** Must optimize for low-end devices (3GB RAM)
* **Bad:** Smaller models mean some capability trade-offs
* **Bad:** Device heterogeneity adds complexity
* **Bad:** Requires careful battery/performance optimization

## Implementation Implications

This decision impacts:

1. **Technology choices:** Must use mobile-optimized ML frameworks (ONNX Runtime Mobile, llama.cpp, TFLite)
2. **Model selection:** Limited to models that fit in <2GB RAM and respond in <3 seconds
3. **Architecture:** Offline-first data sync, local vector DB, on-device inference
4. **UX design:** Must be simple enough for low-literacy users, work without tutorials
5. **Content strategy:** Content packs must be compact and downloadable over slow connections
6. **School nodes:** Become optional accelerators rather than core infrastructure

## Links

* [Vision Document - Section 5: New Core Principles](../product/vision.md)
* [Vision Document - Section 6.1: Learner Phone Stack](../product/vision.md)
* [Phone Architecture Document](../architecture/phone-architecture.md) (to be created)
* [ADR-002: Offline-First Design](ADR-002-offline-first-design.md)
* [ADR-003: Edge Device as Accelerator](ADR-003-edge-device-as-accelerator.md)

---

## References

Key sections from vision document that informed this decision:

> **5.1 Phone Is The Primary Compute Surface**  
> Because phones are:
> - Already owned
> - Already charged
> - Already trusted
> - Already familiar

> **3.4 Deployment Reality**  
> What kills most "good intention tech":
> - No update mechanism
> - No support structure
> - Too complex for schools to operate
> - Requires cloud accounts or payment methods
> - Needs training
