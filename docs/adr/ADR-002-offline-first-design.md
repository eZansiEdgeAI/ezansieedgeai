# ADR-002: Offline-First Design

* **Status:** Accepted
* **Date:** 2026-02-16
* **Decision Makers:** Project Team
* **Technical Story:** Design for South African connectivity and data cost realities

## Context and Problem Statement

Our target users face significant connectivity challenges:
- Expensive mobile data
- Inconsistent or no internet access at schools
- Load shedding affecting WiFi availability
- Rural areas with limited coverage

**Question:** Should our app require internet connectivity, work best online with offline fallback, or be truly offline-first?

## Decision Drivers

* **Data costs:** Mobile data is expensive and often prohibitive for our target users
* **Connectivity gaps:** Many schools and homes have no reliable internet
* **Load shedding:** Power outages affect network infrastructure
* **Usage patterns:** Homework happens at home where internet may not be available
* **Educational value:** Learning should not depend on connectivity
* **Privacy:** Offline-first naturally supports privacy (no data leaves device)
* **User trust:** Parents and teachers more comfortable with no cloud dependency

## Considered Options

1. **Cloud-Required:** All processing happens in cloud, requires internet
2. **Cloud-First with Offline Cache:** Primary functionality online, limited offline fallback
3. **Offline-First with Cloud Enhancement:** Fully functional offline, optional online features
4. **Offline-Only:** No internet connectivity used at all

## Decision Outcome

**Chosen option:** "Offline-First with Cloud Enhancement" (with V1 being Offline-Only)

The app must work **completely offline** after initial installation. All core functionality (asking questions, getting explanations, accessing content) works with zero internet connectivity. Future cloud/online features are optional enhancements that gracefully degrade when unavailable.

**V1 Scope:** Offline-only. No online features at all.

### Reasoning

1. **Alignment with mission:** "If learners have nothing, they should still have something." Requiring internet excludes exactly the learners we're trying to serve.

2. **Data cost reality:** Even if connectivity is available, the data cost of repeated cloud API calls is prohibitive for our target users.

3. **Technical feasibility:** Modern phones can run small LLMs locally. Offline is now technically possible where it wasn't a few years ago.

4. **Reliability:** Offline-first means the app works 100% of the time, not only when connected.

5. **Trust and adoption:** No cloud dependency means no privacy concerns, no accounts, no tracking - all barriers to adoption.

### Positive Consequences

* **Works everywhere:** App functions in schools with no internet, homes without connectivity, during load shedding
* **Zero ongoing data cost:** No mobile data charges for using the app
* **Privacy by default:** No learner data transmitted anywhere
* **Reliable:** Works exactly the same whether connected or not
* **Fast:** No network latency, instant responses
* **Simpler architecture:** No authentication, no sync logic, no online/offline mode switching

### Negative Consequences

* **Larger initial download:** Must include model + content pack in initial install (~500MB)
* **Update complexity:** Content updates must be delivered via packs, not dynamic cloud sync
* **Feature constraints:** Can't leverage cloud-only capabilities (large models, real-time updates)
* **Storage requirements:** All content must fit on device storage
* **Limited personalization:** Can't learn from aggregate usage patterns across users

## Pros and Cons of the Options

### Cloud-Required

* **Good:** Access to powerful models and unlimited compute
* **Good:** Easy to update and improve
* **Good:** Small app download size
* **Bad:** Excludes users without connectivity (most of our target users)
* **Bad:** Ongoing data costs
* **Bad:** Privacy concerns
* **Bad:** Completely misaligned with mission

### Cloud-First with Offline Cache

* **Good:** Best experience when online
* **Good:** Some offline capability
* **Bad:** Confusing UX (different features available based on connectivity)
* **Bad:** Still has data costs for primary use
* **Bad:** Offline mode feels "degraded" or "second-class"
* **Bad:** Complex to build (two modes to test and maintain)

### Offline-First with Cloud Enhancement (Chosen)

* **Good:** Full functionality without internet
* **Good:** Optional enhancements when connectivity available
* **Good:** No data cost for core use
* **Good:** Privacy-preserving by default
* **Good:** Works everywhere
* **Good:** Graceful enhancement rather than degradation
* **Bad:** Larger initial download
* **Bad:** Content updates more complex
* **Bad:** Can't leverage some cloud-only features

### Offline-Only

* **Good:** Maximum simplicity
* **Good:** Perfect privacy
* **Good:** Zero data costs ever
* **Bad:** No path to add optional online enhancements later
* **Bad:** Misses opportunities for future features (content marketplace, teacher connections, etc.)

## Implementation Implications

### Architecture

1. **All data local:**
   - Content packs stored locally
   - Vector database stored locally
   - Model files stored locally
   - Learner preferences stored locally

2. **No authentication required:**
   - No accounts
   - No login
   - No cloud services

3. **Content pack architecture:**
   - Versioned, self-contained packages
   - Delivered via: initial install, USB/SD card transfer, local WiFi (school node), or optional download
   - Cryptographic signatures for integrity

4. **Local processing:**
   - Embedding generation on device
   - Vector search on device
   - LLM inference on device
   - All computation happens locally

### Technology Choices

- **On-device ML:** llama.cpp (GGUF), ONNX Runtime Mobile, or TensorFlow Lite
- **Local vector DB:** SQLite with vector extension or custom implementation
- **Storage:** Android local storage, encrypted if needed
- **No network libraries needed** for V1

### Content Updates

Three mechanisms (none require internet):

1. **App update:** New version of app includes updated content
2. **SD card/USB:** Content packs copied manually
3. **Local WiFi:** School edge node distributes updates over LAN

### Future Online Features (Optional)

If/when we add optional online features:
- Must gracefully degrade when offline
- No features should require online
- Examples: content pack marketplace, community contributions, teacher dashboards

## Testing Implications

- **Airplane mode testing:** Must test ALL functionality with airplane mode enabled
- **No mocks for network:** Since nothing should use network
- **Storage testing:** Test with limited storage scenarios
- **Performance testing:** All on target hardware (no cloud performance dependency)

## Links

* [Vision Document - Section 5.2: Offline First Always](../product/vision.md)
* [ADR-001: Phone-First Architecture](ADR-001-phone-first-architecture.md)
* [ADR-004: Content Pack Architecture](ADR-004-content-pack-architecture.md)
* [Phone Architecture Document](../architecture/phone-architecture.md) (to be created)

---

## References

From vision document:

> **5.2 Offline First Always**  
> System must work:
> - Without internet
> - Without accounts
> - Without cloud dependency

> **Key realities we are designing for:**
> - Expensive mobile data
> - Inconsistent connectivity
> - Low-end device availability

> **3.5 Adoption Reality**  
> Even free tech fails if:
> - It is complicated
> - It drains battery
> - It needs setup
> - It feels slow
> - It breaks trust (privacy / tracking fears)

## Notes

This decision fundamentally shapes the product. It's not just about being "offline capable" - it's about being offline-native and treating online as the optional enhancement, not the other way around.

This aligns with our core mission: accessibility for all, regardless of connectivity or economic status.
