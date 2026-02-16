# eZansiEdgeAI School Edge Node

Optional edge device server providing enhanced services for learner mobile apps over local WiFi.

## Overview

The school edge node is an **optional** component that runs on local school infrastructure to provide:
- Content pack distribution and updates
- Speech-to-text services (future)
- Text-to-speech services (future)
- Optional heavier AI computation offload

**Important:** The learner mobile app works fully offline without this node. This is purely an enhancement for schools that have the infrastructure.

## Design Principles

1. **Offline-Only:** Works without internet connectivity
2. **Zero-Config:** Automatic discovery via mDNS/Bonjour
3. **Low Cost:** Runs on cheap hardware (Raspberry Pi, mini PC, or router)
4. **No Internet Required:** All services work locally
5. **Optional:** Learner apps work without it

## Technical Specifications (Planned)

- **Platform:** Linux (Debian/Ubuntu)
- **Language:** Python or Go (TBD)
- **Services:**
  - HTTP/REST API for content distribution
  - Optional gRPC for low-latency services
  - mDNS/Bonjour for service discovery

## Deployment Options

### Option 1: Raspberry Pi
- Raspberry Pi 4 (4GB+ RAM recommended)
- microSD card (32GB+)
- Power supply
- Case

### Option 2: Mini PC
- Any low-power x86_64 mini PC
- 4GB+ RAM
- 32GB+ storage

### Option 3: Router with Linux
- OpenWrt-compatible router
- Sufficient storage and RAM

## Services (Planned)

### 1. Content Pack Server
- Serve content packs over HTTP
- Version management
- Delta updates

### 2. Speech Services (Future)
- Speech-to-text (Whisper or similar)
- Text-to-speech (local TTS)

### 3. Compute Offload (Future)
- Optional larger model inference
- Batch processing support

## Development Status

🚧 **Status:** Future Phase

This component is planned for Phase 3 (Weeks 11-13) and is not critical for V1.

## Setup Instructions

*Coming soon - not yet implemented*

## Related Documentation

- [Edge Device Architecture](../../docs/architecture/edge-device-architecture.md)
- [Deployment Modes](../../docs/architecture/deployment-modes.md)
- [ADR-003: Edge Device as Accelerator](../../docs/adr/ADR-003-edge-device-as-accelerator.md)
- [School Node Design Story](../../docs/development/backlog-v1.md#story-018-design-school-node-architecture)

## Contributing

Please see [CONTRIBUTING.md](../../CONTRIBUTING.md) for development guidelines.

## License

*To be added - Open source license*
