# Applications

This directory contains the application components of eZansiEdgeAI.

## Directory Structure

### learner-mobile/
Android mobile application for learners. This is the primary interface where learners ask questions and receive AI-powered explanations.

**Key Features:**
- Offline-first design
- Works on Android 10+ devices with 3GB RAM
- Local content pack loading
- On-device AI inference
- Privacy-focused (no tracking, all data local)

**Status:** Not yet implemented

---

### school-edge-node/
Optional edge device application that runs on school WiFi networks to provide enhanced services.

**Key Features:**
- Content pack distribution
- Speech-to-text services (future)
- Text-to-speech services (future)
- Optional heavier computation offload
- Works fully offline (no internet required)

**Status:** Not yet implemented

---

## Development Principles

1. **Offline First**: All apps must work without internet connectivity
2. **Privacy First**: No learner data leaves the device without explicit consent
3. **Low Resource**: Target 3GB RAM Android devices
4. **Simple UX**: Intuitive for learners who may have limited tech experience
5. **Open Source**: All code is open source and auditable

## Getting Started

Refer to the README in each subdirectory for specific setup instructions.

## Related Documentation

- [Vision Document](../docs/product/vision.md)
- [Architecture Overview](../docs/architecture/system-overview.md)
- [Development Backlog](../docs/development/backlog-v1.md)
