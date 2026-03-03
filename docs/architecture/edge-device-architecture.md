# eZansiEdgeAI: Edge Device Architecture

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Deployment Teams, School Technical Contacts

---

## 1. Purpose

The school edge device is an **optional capability accelerator** — it enhances the learning experience when present but is never a dependency for core learning to function.

This document details the edge device stack, its services, and the critical constraint that phone learning must continue to work whether or not the node is reachable.

---

## 2. The Critical Constraint

> **If the school node is offline, unreachable, or absent — phone learning must still work fully.**

This is not a fallback behaviour. It is an architectural requirement. The phone stack must be complete and functional in isolation. The edge node only adds to what is already working.

---

## 3. Edge Device Stack Overview

```
┌──────────────────────────────────────────────────────┐
│               WIFI SERVICE LAYER                     │
│  Local API Gateway                                   │
│  Content Distribution Service                        │
│  Update Server                                       │
├──────────────────────────────────────────────────────┤
│                  AI SERVICES                         │
│  Shared Speech-to-Text (STT)                         │
│  Shared Text-to-Speech (TTS)                         │
│  Optional Larger Inference Model                     │
├──────────────────────────────────────────────────────┤
│                 DATA SERVICES                        │
│  Shared Content Cache                                │
│  School Knowledge Base                               │
└──────────────────────────────────────────────────────┘
```

---

## 4. WiFi Service Layer

The WiFi Service Layer is the entry point for phones connecting over the school's local WiFi.

### 4.1 Local API Gateway
- Lightweight HTTP service (LAN only — no internet exposure)
- Routes phone requests to appropriate backend services on the node
- Handles request queuing if multiple phones connect simultaneously
- Health check endpoint phones use to detect node availability
- No authentication required in V1 (trusted LAN environment)

### 4.2 Content Distribution Service
- Hosts the master content pack repository for the school
- Responds to phone requests for pack manifests and pack downloads
- Supports differential / incremental pack updates (reduce transfer size)
- Phones pull on demand — no push to phones
- Content packs are the same format used for offline phone storage

### 4.3 Update Server
- Distributes app updates and model updates over LAN
- Phones check for updates when connected; download in background
- Update packages are signed to prevent tampering
- Internet-seeded updates arrive here first, then distribute to phones locally
- Designed to work even when the school's internet connection is down

---

## 5. AI Services

AI Services on the edge node provide capabilities that are too expensive or complex to run on every phone independently.

### 5.1 Shared Speech-to-Text (STT)
- Processes voice input from learner phones over LAN
- Runs a quantized speech recognition model on the edge device's hardware
- Returns text transcript to the requesting phone
- Phone continues with standard offline query flow after receiving transcript
- Graceful fallback: if STT unavailable, phone falls back to text input

### 5.2 Shared Text-to-Speech (TTS)
- Converts text responses to audio for playback on learner phone
- Supports multiple voices; language selection per request
- Synthesised audio streamed back over LAN to the requesting phone
- Graceful fallback: if TTS unavailable, phone displays text response only

### 5.3 Optional Larger Inference Model
- A larger quantized LLM that can handle more complex queries
- Used when a phone's on-device model cannot generate a satisfactory response
- Phone requests a "cloud-style" inference from the node, receives response over LAN
- The phone's local model remains the primary; this is supplementary only
- Not required for V1 core functionality

---

## 6. Data Services

### 6.1 Shared Content Cache
- Caches content packs that have been downloaded from internet (when available)
- Serves as the distribution point for all phones on the school network
- Ensures that internet bandwidth is consumed once, not once per phone
- Persists content between internet outages

### 6.2 School Knowledge Base
- Optional: school-specific supplementary content authored by teachers
- Local additions to content packs (worked examples, local context)
- Distributed to phones the same way as standard content packs
- Not required in V1 — placeholder for future capability

---

## 7. Target Hardware for Edge Node

The edge device should be accessible and maintainable without IT expertise.

| Property | Minimum | Target |
|----------|---------|--------|
| Form factor | Mini PC / NUC | Mini PC / NUC |
| OS | Linux (Ubuntu / Debian) | Ubuntu LTS |
| RAM | 8 GB | 16 GB |
| Storage | 128 GB SSD | 256 GB SSD |
| Network | 100 Mbps LAN | Gigabit LAN |
| Power | Low-power mode | UPS-compatible |

**Alternative deployment on existing hardware:**
- The edge node software can also run on:
  - A spare laptop left in the school office
  - A Raspberry Pi 4 / 5 (limited AI services)
  - An existing school server (if available)

---

## 8. Node Availability and Resilience

| Scenario | Phone Behaviour |
|----------|----------------|
| Node online, reachable | Phone uses node for STT/TTS/content sync |
| Node online but overloaded | Phone falls back to local-only mode |
| Node offline (load shedding) | Phone operates fully independently |
| Node never installed | Phone operates fully independently |

Discovery: phones broadcast a LAN probe on startup. If no response within 2 seconds, phone assumes node is absent and continues in offline-only mode. No error shown to learner.

---

## 9. Related Documents

- [System Overview](./system-overview.md)
- [Phone Architecture](./phone-architecture.md)
- [Deployment Modes](./deployment-modes.md)
- [ADR-003 — Edge Device as Accelerator](../adr/ADR-003-edge-device-as-accelerator.md)
