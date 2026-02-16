# Edge Device Models

AI models for optional school edge nodes with more compute resources.

## Target Specifications

- **RAM:** Can use more RAM than phone models
- **Storage:** <5GB per model
- **Performance:** Real-time for speech services
- **Format:** PyTorch, ONNX, or native format
- **Device:** Linux server (Raspberry Pi 4+, mini PC, or router)

## Purpose

Edge device models provide enhanced capabilities that are too resource-intensive for phones:
- Speech-to-text (Whisper or similar)
- Text-to-speech (Piper, Coqui, or similar)
- Optional larger LLM for complex queries

**Important:** These are optional enhancements. Core app functionality works without edge devices.

## Model Files

Model files are **not stored in git** due to size. For development and deployment:
- Download separately
- Store in this directory locally (gitignored)
- Distribute via edge node setup scripts

## Candidate Models (Future Phase 3)

### Speech-to-Text

1. **Whisper (Base or Small)**
   - Size: 140MB (tiny), 460MB (base), 1.4GB (small)
   - Use case: Real-time transcription
   - Status: Future evaluation (Phase 3)
   - License: MIT

2. **Vosk**
   - Size: ~50MB (small model)
   - Use case: Lightweight alternative
   - Status: Alternative option
   - License: Apache 2.0

### Text-to-Speech

1. **Piper**
   - Size: ~10-50MB per voice
   - Use case: High-quality local TTS
   - Status: Primary candidate for Phase 3
   - License: MIT

2. **Coqui TTS**
   - Size: Varies by model
   - Use case: More natural voices
   - Status: Alternative if licensing allows
   - License: MPL 2.0

### Optional Larger LLM

1. **Phi-2 (2.7B, full precision or 8-bit)**
   - Size: 5GB (full), 2.5GB (8-bit)
   - Use case: More complex reasoning for advanced queries
   - Status: Optional enhancement

2. **Mistral 7B (quantized)**
   - Size: 4-5GB
   - Use case: Even better reasoning
   - Status: If hardware permits

## Development Status

🚧 **Status:** Future Phase (Phase 3, Weeks 11-13)

Edge device functionality is not required for V1. Development priorities:
1. **Phase 1-2:** Phone-only implementation
2. **Phase 3:** Add edge device services
3. **Future:** Expand edge capabilities

## Edge Node Architecture

See [Edge Device Architecture](../../docs/architecture/edge-device-architecture.md) (to be created) for full design.

Services provided:
- Local API for content distribution
- Speech service APIs (STT/TTS)
- Optional compute offload
- Update distribution

## Deployment Options

### Option 1: Raspberry Pi 4
- 4GB or 8GB RAM recommended
- Can run Whisper Base + Piper
- Affordable (~$100 with accessories)

### Option 2: Mini PC
- 8GB+ RAM
- Can run larger models
- More compute for heavier workloads

### Option 3: Router with OpenWrt
- Limited capability
- Content distribution only
- Lowest cost option

## Development Setup

*To be documented when Phase 3 begins*

## Testing Checklist

When edge node is implemented:
- [ ] Service discovery (mDNS)
- [ ] API response times
- [ ] Concurrent request handling
- [ ] Graceful degradation when offline
- [ ] Phone app fallback when node unavailable

## Documentation

- [ADR-003: Edge Device as Accelerator](../../docs/adr/ADR-003-edge-device-as-accelerator.md)
- [Edge Device Architecture](../../docs/architecture/edge-device-architecture.md) (to be created)
- [Deployment Modes](../../docs/architecture/deployment-modes.md) (to be created)
- [STORY-018: Design School Node Architecture](../../docs/development/backlog-v1.md#story-018)

## Download Instructions

*To be added in Phase 3*

## License Compliance

All models must allow:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

## Notes

⚠️ **Important:** 
- Do not commit model files to git
- Edge node is optional - app works without it
- Priority: Get phone app working first
