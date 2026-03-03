# eZansiEdgeAI: Success Metrics

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Product Owners, NGO Partners

---

## 1. Purpose

This document defines what success looks like for eZansiEdgeAI — at V1 launch and beyond. Metrics are deliberately simple and grounded in real-world usability, not vanity statistics.

> Success is not a flashy demo.  
> Success is a learner using this offline, on a normal phone, for real homework, without help from us.

---

## 2. V1 Success Metrics

V1 is successful when all of the following are true:

### 2.1 Works Offline Reliably
- [ ] App installs and runs fully without any internet connection
- [ ] Questions are answered without any network activity
- [ ] App startup completes without connectivity
- [ ] No features silently fail when offline — degradation is visible and graceful
- [ ] Verified on at least 3 different Android devices in the target hardware range

### 2.2 Runs on Low-Mid Android Devices
- [ ] Functional on Android 10+, ~3GB RAM devices
- [ ] LLM explanation generated within 8 seconds on minimum spec device
- [ ] No out-of-memory crashes during normal use
- [ ] App does not cause device overheating under sustained 10-minute use
- [ ] Battery impact is acceptable for a 30-minute study session

### 2.3 Teachers Can Install Without IT Support
- [ ] Installation is a single APK — no additional setup steps
- [ ] No account creation or login required
- [ ] Content pack installation is self-explanatory
- [ ] A non-technical adult can complete full setup in under 10 minutes
- [ ] Verified with at least 2 teacher-profile testers

### 2.4 Learners Can Use Without Training
- [ ] A Grade 6 learner can ask their first question without instruction
- [ ] Response quality is legible and appropriate for a Grade 6 reading level
- [ ] Learner can navigate between questions and content naturally
- [ ] No dead ends — every screen has a clear next action
- [ ] Verified with at least 3 learner-profile testers

### 2.5 No Cost Barrier
- [ ] App is freely available (open source, no store paywall)
- [ ] No in-app purchases or subscription prompts
- [ ] No mandatory internet connectivity that would require data spend
- [ ] Edge node software is free to install and operate
- [ ] No external service accounts required

### 2.6 Content Is Accurate and Curriculum-Grounded
- [ ] All Grade 6 Mathematics content is CAPS-aligned
- [ ] At least one full term of content is available in V1 pack
- [ ] Model responses are grounded in retrieved content — not invented
- [ ] Content reviewed by at least one subject matter expert before release

---

## 3. V1 Anti-Metrics (What We Are Not Measuring in V1)

We explicitly do not measure:

- Number of users / installs (no analytics in V1)
- Session duration (no tracking in V1)
- Learning outcomes / test scores (not our role in V1)
- Engagement rates (no telemetry in V1)
- Model accuracy benchmarks (we measure real-world usability, not benchmark performance)

These may become relevant in future phases — with learner consent and local-only storage.

---

## 4. Long-Term Metrics (Post-V1)

These are indicators of sustained real-world impact. They are directional, not V1 commitments.

### 4.1 Reach
- Number of schools where the app is actively used (self-reported by partners)
- Number of content packs distributed (tracked via pack manifest versioning)
- Geographic spread (provinces / districts reached)

### 4.2 Content Quality
- Number of CAPS-aligned content packs available
- Subject and grade coverage
- Pack update frequency (content kept current)
- Community contribution rate (teacher-authored packs)

### 4.3 Language Inclusion
- Number of supported interface languages
- Number of content packs available in languages other than English
- Learner-reported language preference usage

### 4.4 Infrastructure Independence
- Percentage of usage occurring in Mode A (phone only) — indicates true offline reach
- Edge node uptime (where installed) — indicates reliability of school node
- Pack distribution rate over LAN vs internet — indicates data cost savings

### 4.5 Community Health
- Number of active contributors to the open source project
- Number of content pack authors (non-developer contributors)
- Issue resolution time
- Documentation coverage

---

## 5. Definition of Done (V1 Release Gate)

V1 is releasable when:

1. All V1 success metrics (Section 2) are verified
2. No known offline-breaking bugs
3. Grade 6 Maths Term 1 content pack is complete and reviewed
4. Installation guide is complete and tested
5. Open source licence confirmed on all dependencies
6. Privacy statement is accurate and visible in app
7. At least one real-world test deployment completed (school or community)

---

## 6. Related Documents

- [Product Vision](./vision.md)
- [Constraints](./constraints.md)
- [User Personas](./user-personas.md)
- [V1 Backlog](../development/backlog-v1.md)
