# AI Models

This directory contains AI model files and related resources for the eZansiEdgeAI system.

## Directory Structure

### phone-models/
Models optimized for on-device inference on Android phones (3GB RAM target).

**Planned Models:**
- Small quantized LLM (GGUF or ONNX format)
- Embedding model for semantic search
- Prompt templates

**Status:** Research phase (See STORY-004 in backlog)

---

### edge-models/
Optional larger models for school edge nodes with more compute resources.

**Planned Models:**
- Speech-to-text model (Whisper or similar)
- Text-to-speech model
- Optional larger LLM for more complex queries

**Status:** Future phase

---

## Model Selection Criteria

### Phone Models
- **Size:** <500MB per model
- **RAM:** Peak usage <2GB
- **Inference:** <3s for typical explanation generation
- **Format:** GGUF (via llama.cpp) or ONNX Runtime Mobile
- **License:** Open source, commercial use allowed

### Edge Models
- **Size:** <5GB per model
- **Performance:** Real-time for speech services
- **Format:** PyTorch, ONNX, or native format
- **License:** Open source

## Candidate Models Under Evaluation

### LLMs for Phone
1. **TinyLlama** (1.1B parameters, quantized to 4-bit)
   - Size: ~600MB
   - Good for simple explanations
   
2. **Phi-2** (2.7B parameters, quantized to 4-bit)
   - Size: ~1.5GB
   - Better reasoning, may be too large

3. **Qwen-1.5-0.5B** (quantized)
   - Size: ~300MB
   - Very small, may lack capability

4. **MobileLLM** (optimized for mobile)
   - Specifically designed for on-device use
   - Need to evaluate availability

### Embedding Models
1. **all-MiniLM-L6-v2** (ONNX)
   - Size: ~23MB
   - Fast, good quality
   
2. **paraphrase-multilingual-MiniLM** (for future multilingual support)
   - Size: ~100MB

## Model Files

⚠️ **Note:** Model files are NOT stored in this git repository due to size.

Model files should be:
- Downloaded separately
- Stored in this directory locally for development
- Distributed via content packs or separate download for production

## .gitignore Rules

The following patterns are ignored to prevent accidentally committing large model files:
```
*.bin
*.gguf
*.onnx
*.pt
*.pth
*.safetensors
*.ckpt
```

## Documentation

- [Model Selection Research](../docs/architecture/model-selection-research.md) - Research comparing model options
- [ADR-004: Content Pack Architecture](../docs/adr/ADR-004-content-pack-architecture.md) - How models are packaged
- [Storage Analysis](../docs/architecture/storage-analysis.md) - Storage footprint validation

## Development Notes

### Testing with Models Locally

1. Download test models to appropriate subdirectory
2. Models are gitignored and won't be committed
3. Update README in subdirectory with download instructions
4. Test with Android Virtual Device or physical device

### Model Performance Testing

Key metrics to measure:
- Cold start time (first inference)
- Warm inference time (subsequent inferences)
- Peak memory usage
- Battery impact per inference
- Model file size on disk

## Related Documentation

- [Phone Architecture](../docs/architecture/phone-architecture.md)
- [STORY-004: Research On-Device Inference Options](../docs/development/backlog-v1.md#story-004)
- [STORY-006: Validate Storage Footprint Limits](../docs/development/backlog-v1.md#story-006)

## Contributing

When adding models or model evaluation:
1. Document model source and license
2. Include performance benchmarks on target hardware
3. Update this README with findings
4. Create or update ADR if architectural decision is made

## License

See individual model licenses. All models must be open source with commercial use allowed.
