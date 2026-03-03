# eZansiEdgeAI: Deployment Modes

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Deployment Teams, NGO Partners

---

## 1. Purpose

eZansiEdgeAI is designed to work across a spectrum of infrastructure availability. This document defines three deployment modes, from the most constrained (phone only) to the most capable (community hub). All modes support full offline learning.

---

## 2. Mode Summary

| Mode | Infrastructure | Primary Use Case | Learning Capability |
|------|---------------|-----------------|-------------------|
| **A — Phone Only** | Phone only | Worst case / home use | Full offline learning |
| **B — Phone + School Edge WiFi** | Phone + school node | Primary school deployment | Full offline + enhanced services |
| **C — Community Hub Device** | Shared hub device | Library / NGO / community | Shared access point |

---

## 3. Mode A — Phone Only

### When It Applies
- No school edge node is installed or available
- Learner is studying at home or in transit
- School node is offline due to load shedding or hardware failure
- Fallback when WiFi is unavailable at school

### What the Learner Gets
- Full curriculum content retrieval from locally installed packs
- Full LLM-powered explanation generation (on-device)
- Personal learning profile with preference-shaped responses
- Worked examples and step-by-step breakdowns
- All content from last pack installation

### What Is Not Available in This Mode
- Voice input (STT) — text input only in V1
- Voice output (TTS) — text display only in V1
- Content pack updates (until next WiFi connection)
- Optional larger model inference

### Guidance
> Mode A is not a degraded experience — it is the designed baseline.  
> All V1 core functionality must work in Mode A.  
> If a feature cannot work in Mode A, it is not a core V1 feature.

### Setup Requirements
- Install app via APK sideload or trusted distribution
- Download and install at least one content pack
- No internet connection required after initial setup

---

## 4. Mode B — Phone + School Edge WiFi

### When It Applies
- School has an edge node installed and running
- Learner is physically at school with WiFi access
- Standard daytime school usage

### What the Learner Gets
- Everything in Mode A, plus:
- Voice input via school node STT service
- Voice output via school node TTS service
- Automatic content pack updates (new terms, corrections)
- App and model updates distributed over LAN
- Optional: more powerful inference for complex queries

### What the School Gets
- Central content distribution point (one internet download → many phones)
- LAN-based update distribution (reduces per-device data cost)
- Optional: school-specific supplementary content authored by teachers

### Transition Behaviour
- Phone automatically detects node presence on LAN at startup
- No learner action required to switch between Mode A and Mode B
- If node becomes unavailable mid-session, phone continues in Mode A silently

### Setup Requirements
- Edge node hardware installed at school (mini PC / NUC / laptop)
- Edge node software installed and running
- School WiFi accessible to learner phones
- Content packs loaded onto edge node

### Guidance
> Mode B is the primary target deployment.  
> Design and test all features in Mode A first.  
> Mode B features are enhancements — never replacements for core function.

---

## 5. Mode C — Community Hub Device

### When It Applies
- A public library, NGO, community centre, or clinic provides a shared access point
- Learners visit the location to sync content packs and app updates
- The hub device may itself be an Android device or a small server

### What the Learner Gets
- Content pack sync to their personal phone (bring phone, connect to hub WiFi)
- App and model updates
- Potentially: access to a larger shared device for study sessions
- All Mode A functionality continues at home after syncing

### What the Community Hub Gets
- Serves as a community content distribution node
- Can receive internet-seeded pack updates when connectivity is available
- Operates as a standalone node when internet is absent

### Hub Device Options
- Android tablet or phone running hub mode (lightweight)
- Raspberry Pi 4/5 running edge node software
- Mini PC / laptop running full edge node stack
- Existing community server or NAS device

### Guidance
> Mode C extends reach beyond the school.  
> Treat hub devices as Mode B edge nodes in a community context.  
> Hub devices must be able to operate without internet after initial seed.

---

## 6. Mode Transition Summary

```
Mode A ──────────────────────────────── always works
  │
  ▼ (WiFi + edge node detected)
Mode B ──────────────────────────────── enhanced experience
  │
  ▼ (community location)
Mode C ──────────────────────────────── shared access point
```

Transitions are **automatic and transparent** to the learner. No configuration changes required on the phone when moving between environments.

---

## 7. Deployment Checklist by Mode

### Mode A (Phone Only)
- [ ] App installed (APK or trusted source)
- [ ] At least one content pack installed
- [ ] Learner profile created (optional but recommended)

### Mode B (School Node)
- [ ] Mode A complete for all learner phones
- [ ] Edge node hardware in place
- [ ] Edge node software installed and tested
- [ ] School WiFi accessible to learner phones
- [ ] Content packs loaded on edge node
- [ ] Node tested: phone discovers node on startup

### Mode C (Community Hub)
- [ ] Hub hardware in place
- [ ] Edge node software installed
- [ ] Initial content pack seed loaded (USB or internet)
- [ ] Hub WiFi broadcast visible to visiting phones
- [ ] Phones verified to sync packs successfully

---

## 8. Related Documents

- [System Overview](./system-overview.md)
- [Edge Device Architecture](./edge-device-architecture.md)
- [Phone Architecture](./phone-architecture.md)
- [Constraints](../product/constraints.md)
