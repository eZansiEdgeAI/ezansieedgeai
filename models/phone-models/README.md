# Phone Models

AI models optimized for on-device inference on Android phones.

## Target Specifications

- **RAM:** Peak usage <2GB
- **Storage:** <500MB per model
- **Inference:** <3 seconds for typical queries
- **Format:** GGUF (via llama.cpp) or ONNX Runtime Mobile
- **Device:** Android 10+, 3GB RAM minimum

## Model Files

Model files are **not stored in git** due to size. They should be:
- Downloaded separately for development
- Distributed via content packs or separate downloads for production
- Stored in this directory locally (gitignored)

## Candidate Models (Under Evaluation)

### Small LLMs for Text Generation

1. **TinyLlama (1.1B, 4-bit quantized)**
   - Size: ~600MB
   - Use case: Simple explanations
   - Status: To be evaluated (STORY-004)

2. **Phi-2 (2.7B, 4-bit quantized)**
   - Size: ~1.5GB
   - Use case: Better reasoning
   - Status: To be evaluated (STORY-004)

3. **Qwen-1.5-0.5B (4-bit quantized)**
   - Size: ~300MB
   - Use case: Ultra-light option
   - Status: To be evaluated (STORY-004)

4. **MobileLLM (optimized for mobile)**
   - Size: TBD
   - Use case: Specifically designed for on-device use
   - Status: To be evaluated (STORY-004)

### Embedding Models

1. **all-MiniLM-L6-v2 (ONNX)**
   - Size: ~23MB
   - Use case: Semantic search / retrieval
   - Status: Primary candidate

2. **paraphrase-multilingual-MiniLM (ONNX)**
   - Size: ~100MB
   - Use case: Future multilingual support
   - Status: Future consideration

## Model Selection Process

See [STORY-004: Research On-Device Inference Options](../../docs/development/backlog-v1.md#story-004) for the research and evaluation process.

Key evaluation criteria:
1. Performance on target hardware (3GB RAM Android)
2. Inference latency (<3s target)
3. Memory footprint (peak <2GB)
4. Model file size (<500MB)
5. License (open source, commercial use allowed)
6. Quality of generated explanations

## Development Setup

### For Local Testing

1. Download test models to this directory
2. Models are automatically gitignored
3. Update documentation with download instructions for team

### Testing Checklist

When testing a model:
- [ ] Cold start time (first inference)
- [ ] Warm inference time (subsequent inferences)
- [ ] Peak memory usage (via Android Profiler)
- [ ] Battery impact per inference
- [ ] File size on disk
- [ ] Quality of explanations (on math problems)
- [ ] Behavior on edge cases (very long input, out-of-domain questions)

## Prompt Templates

Prompt templates for each model should be stored in `apps/learner-mobile/src/main/assets/prompts/` or similar, not here.

## Documentation

- [Model Selection Research](../../docs/architecture/model-selection-research.md) (to be created)
- [ADR-001: Phone-First Architecture](../../docs/adr/ADR-001-phone-first-architecture.md)
- [Storage Analysis](../../docs/architecture/storage-analysis.md) (to be created)

## Download Instructions

*To be added once models are selected*

Example:
```bash
# TinyLlama 4-bit GGUF
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

# all-MiniLM-L6-v2 ONNX
wget https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/onnx/model.onnx
```

## License Compliance

All models must have licenses that allow:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

Common acceptable licenses:
- MIT
- Apache 2.0
- Creative Commons (appropriate variants)

## Notes

⚠️ **Important:** Do not commit model files to git. The .gitignore is configured to prevent this, but be mindful of file sizes when committing.
