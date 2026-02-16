# eZansiEdgeAI V1 Backlog

## Epic 1: Project Foundation
**Priority:** CRITICAL  
**Goal:** Establish core project structure and documentation for development to begin

### Stories

#### STORY-001: Initialize Project Structure
**Priority:** HIGH  
**Estimate:** 2 days  
**Agent:** Infrastructure Agent

**Description:**  
Set up the foundational directory structure and README files for all major components.

**Acceptance Criteria:**
- [ ] All directories from vision document created (apps/, models/, docs/architecture/, docs/adr/)
- [ ] README.md files in each directory explaining purpose
- [ ] .gitignore configured for mobile/node projects
- [ ] License file added (appropriate open source license)

**Technical Notes:**
- Follow structure from vision document section "New Repository Structure"
- Ensure consistent documentation style

---

#### STORY-002: Create Architecture Documentation
**Priority:** HIGH  
**Estimate:** 3 days  
**Agent:** Documentation Agent

**Description:**  
Document the system architecture based on the strategic direction in the vision.

**Acceptance Criteria:**
- [ ] docs/architecture/system-overview.md created
- [ ] docs/architecture/phone-architecture.md created
- [ ] docs/architecture/edge-device-architecture.md created
- [ ] docs/architecture/deployment-modes.md created
- [ ] All documents reference the vision and constraints

**Technical Notes:**
- Extract content from vision.md sections 6 (Architecture), 9 (Deployment Modes)
- Include diagrams where helpful
- Link to relevant ADRs

---

#### STORY-003: Create Initial ADRs
**Priority:** HIGH  
**Estimate:** 2 days  
**Agent:** Documentation Agent

**Description:**  
Document key architectural decisions made during the strategic direction reset.

**Acceptance Criteria:**
- [ ] ADR-000-template.md created (standard ADR template)
- [ ] ADR-001-phone-first-architecture.md created
- [ ] ADR-002-offline-first-design.md created
- [ ] ADR-003-edge-device-as-accelerator.md created
- [ ] ADR-004-content-pack-architecture.md created

**Technical Notes:**
- Use MADR (Markdown Architectural Decision Records) format
- Reference sections from vision.md that justify each decision
- Include context, decision, and consequences for each

---

## Epic 2: Phase 0 - Feasibility Validation
**Priority:** CRITICAL  
**Goal:** Validate technical feasibility of key architecture decisions (Weeks 1-2)

### Stories

#### STORY-004: Research On-Device Inference Options
**Priority:** HIGH  
**Estimate:** 3 days  
**Agent:** Research Agent

**Description:**  
Investigate and document viable options for running small LLMs on Android devices with 3GB RAM.

**Acceptance Criteria:**
- [ ] Research document comparing GGUF vs ONNX vs TFLite
- [ ] List of candidate models (size, performance, license)
- [ ] Memory footprint analysis for top 3 candidates
- [ ] Recommendation with justification

**Technical Notes:**
- Target: Android 10+, 3GB RAM devices
- Consider: llama.cpp, ONNX Runtime Mobile, TensorFlow Lite
- Models to evaluate: Phi-2, TinyLlama, Qwen, MobileLLM
- Document in docs/architecture/model-selection-research.md

---

#### STORY-005: Prototype Local Embedding + Retrieval
**Priority:** HIGH  
**Estimate:** 4 days  
**Agent:** ML Engineer Agent

**Description:**  
Create proof-of-concept for local vector storage and retrieval on mobile.

**Acceptance Criteria:**
- [ ] POC code demonstrating embedding generation on device
- [ ] POC code demonstrating vector search/retrieval
- [ ] Performance metrics (latency, memory usage)
- [ ] Storage footprint for sample Grade 6 Math content

**Technical Notes:**
- Options to evaluate: SQLite with vector extension, custom solution
- Test with ~100 curriculum content chunks
- Target: <100ms retrieval latency, <50MB storage for test dataset
- Store POC in /tools/feasibility-pocs/

---

#### STORY-006: Validate Storage Footprint Limits
**Priority:** MEDIUM  
**Estimate:** 2 days  
**Agent:** ML Engineer Agent

**Description:**  
Determine realistic storage requirements for V1 Grade 6 Math content pack.

**Acceptance Criteria:**
- [ ] Size estimate for model (quantized GGUF/ONNX)
- [ ] Size estimate for embeddings database
- [ ] Size estimate for Grade 6 Math content
- [ ] Total V1 app package size estimate
- [ ] Comparison with typical app sizes

**Technical Notes:**
- Target total: <500MB initial install
- Document in docs/architecture/storage-analysis.md
- Consider compression options

---

## Epic 3: Phase 1 - Offline Learning Loop (Weeks 3-6)
**Priority:** HIGH  
**Goal:** Deliver basic Android app with pack loading and retrieval pipeline

### Stories

#### STORY-007: Set Up Android Development Environment
**Priority:** HIGH  
**Estimate:** 2 days  
**Agent:** Mobile Engineer Agent

**Description:**  
Initialize Android project with proper structure and dependencies.

**Acceptance Criteria:**
- [ ] Android Studio project created in apps/learner-mobile/
- [ ] Min SDK: Android 10 (API 29)
- [ ] Target SDK: Android 14 (API 34)
- [ ] Gradle configuration complete
- [ ] Basic app shell with navigation structure
- [ ] README with setup instructions

**Technical Notes:**
- Use Kotlin as primary language
- Consider Jetpack Compose for UI
- Set up for offline-first architecture

---

#### STORY-008: Implement Content Pack Loading
**Priority:** HIGH  
**Estimate:** 5 days  
**Agent:** Mobile Engineer Agent

**Description:**  
Create system to load, validate, and manage offline content packs.

**Acceptance Criteria:**
- [ ] Content pack format specification (JSON/YAML)
- [ ] Pack loader module
- [ ] Pack version management
- [ ] Pack integrity validation
- [ ] Local storage management
- [ ] Unit tests

**Technical Notes:**
- Design pack format to include: metadata, content chunks, embeddings
- Support versioning for future updates
- Include sample Grade 6 Math pack (minimal)

---

#### STORY-009: Build Local Retrieval Pipeline
**Priority:** HIGH  
**Estimate:** 5 days  
**Agent:** ML Engineer Agent

**Description:**  
Implement the core retrieval pipeline for finding relevant content based on learner questions.

**Acceptance Criteria:**
- [ ] Query embedding generation
- [ ] Vector similarity search
- [ ] Content ranking algorithm
- [ ] Top-k retrieval implementation
- [ ] Performance within targets (<100ms)
- [ ] Unit and integration tests

**Technical Notes:**
- Use results from STORY-005
- Optimize for battery efficiency
- Cache embeddings where appropriate

---

#### STORY-010: Integrate On-Device LLM
**Priority:** HIGH  
**Estimate:** 5 days  
**Agent:** ML Engineer Agent

**Description:**  
Integrate selected small LLM for explanation generation based on retrieved content.

**Acceptance Criteria:**
- [ ] Model loading and initialization
- [ ] Inference pipeline
- [ ] Prompt template system
- [ ] Context window management
- [ ] Response generation within targets (<3s)
- [ ] Memory management (no leaks)

**Technical Notes:**
- Use model selected in STORY-004
- Implement prompt templates that use retrieved content
- Add safeguards against hallucination

---

## Epic 4: Content Pack Infrastructure
**Priority:** HIGH  
**Goal:** Tools to create and manage content packs

### Stories

#### STORY-011: Design Content Pack Schema
**Priority:** HIGH  
**Estimate:** 2 days  
**Agent:** Data Engineer Agent

**Description:**  
Define the schema and format for content packs including metadata and content structure.

**Acceptance Criteria:**
- [ ] Schema documentation (JSON Schema or similar)
- [ ] Example pack structure
- [ ] Versioning strategy
- [ ] Metadata requirements (subject, grade, language, etc.)
- [ ] Content chunk format

**Technical Notes:**
- Must support: curriculum alignment, difficulty levels, prerequisites
- Consider: multilingual support, accessibility metadata
- Document in docs/architecture/content-pack-schema.md

---

#### STORY-012: Build Pack Builder Tool
**Priority:** MEDIUM  
**Estimate:** 5 days  
**Agent:** Tools Engineer Agent

**Description:**  
Create command-line tool to build content packs from source materials.

**Acceptance Criteria:**
- [ ] CLI tool in tools/content-pack-builder/
- [ ] Parse input content (markdown, text)
- [ ] Generate embeddings
- [ ] Package into pack format
- [ ] Validate pack integrity
- [ ] README with usage examples

**Technical Notes:**
- Should work offline after initial model download
- Support batch processing
- Include validation step

---

## Epic 5: Learner Experience Foundation
**Priority:** MEDIUM  
**Goal:** Basic UI for asking questions and receiving explanations

### Stories

#### STORY-013: Design Learner UI/UX
**Priority:** MEDIUM  
**Estimate:** 3 days  
**Agent:** UI/UX Agent

**Description:**  
Design the learner-facing interface for asking questions and viewing explanations.

**Acceptance Criteria:**
- [ ] Wireframes for main screens (question input, results, history)
- [ ] Design mockups
- [ ] Interaction flows
- [ ] Accessibility considerations
- [ ] Design documentation

**Technical Notes:**
- Keep UI simple and intuitive
- Consider low-literacy users
- Support both text and eventual voice input
- Document in docs/product/ui-design.md

---

#### STORY-014: Implement Question Input Interface
**Priority:** MEDIUM  
**Estimate:** 3 days  
**Agent:** Mobile Engineer Agent

**Description:**  
Build the question input screen with text entry.

**Acceptance Criteria:**
- [ ] Text input screen
- [ ] Question history
- [ ] Input validation
- [ ] Loading states
- [ ] Error handling

**Technical Notes:**
- Keep it simple for V1
- Plan for voice input in future

---

#### STORY-015: Implement Explanation Display
**Priority:** MEDIUM  
**Estimate:** 3 days  
**Agent:** Mobile Engineer Agent

**Description:**  
Build the screen to display explanations and worked examples.

**Acceptance Criteria:**
- [ ] Markdown rendering support
- [ ] Math formula rendering (if needed)
- [ ] Scrollable content
- [ ] Save/bookmark functionality
- [ ] Share functionality (text export)

**Technical Notes:**
- Optimize for readability
- Support different text sizes
- Consider offline viewing of saved explanations

---

## Epic 6: Phase 2 - Content + Personalization (Weeks 7-10)
**Priority:** MEDIUM  
**Goal:** Learner preference engine and first real Grade 6 pack

### Stories

#### STORY-016: Design Learner Preference System
**Priority:** MEDIUM  
**Estimate:** 3 days  
**Agent:** Product Agent

**Description:**  
Design the ethical learner preference system as outlined in vision.

**Acceptance Criteria:**
- [ ] Preference categories defined (explanation style, reading level, examples, pace)
- [ ] Storage schema (local SQLite)
- [ ] Privacy documentation
- [ ] UI for preference management
- [ ] Design document

**Technical Notes:**
- Must be: locally stored, learner-editable, never tracked
- No performance metrics, only preferences
- Document in docs/product/learner-preferences.md

---

#### STORY-017: Create Grade 6 Math Content Pack
**Priority:** HIGH  
**Estimate:** 10 days  
**Agent:** Content Creator Agent

**Description:**  
Build the first real content pack with CAPS-aligned Grade 6 Mathematics content.

**Acceptance Criteria:**
- [ ] Content sourced (or created) covering key Grade 6 Math topics
- [ ] Content chunked appropriately
- [ ] Worked examples for each topic
- [ ] Aligned with CAPS curriculum
- [ ] Pack built and tested in app

**Technical Notes:**
- Topics: Numbers, operations, fractions, geometry, measurement, data handling
- Source from open educational resources where possible
- Ensure copyright compliance
- Size target: <100MB

---

## Epic 7: School Node Prototype (Future)
**Priority:** LOW  
**Goal:** Optional WiFi services for enhanced capabilities

### Stories

#### STORY-018: Design School Node Architecture
**Priority:** LOW  
**Estimate:** 3 days  
**Agent:** Backend Engineer Agent

**Description:**  
Design the school edge node system for local WiFi services.

**Acceptance Criteria:**
- [ ] Architecture document
- [ ] API specification
- [ ] Service discovery mechanism
- [ ] Update distribution design
- [ ] Deployment options (Pi, mini PC, router)

**Technical Notes:**
- Must work without internet
- Zero-config ideal (mDNS/Bonjour)
- Document in docs/architecture/school-node.md

---

## Technical Debt & Infrastructure

### STORY-019: Set Up Testing Infrastructure
**Priority:** HIGH  
**Estimate:** 2 days  

**Description:**  
Set up automated testing for Android app and tools.

**Acceptance Criteria:**
- [ ] Unit test framework configured
- [ ] Integration test framework
- [ ] CI pipeline for tests
- [ ] Code coverage reporting
- [ ] Testing documentation

---

### STORY-020: Create Development Guidelines
**Priority:** MEDIUM  
**Estimate:** 1 day  

**Description:**  
Document coding standards and contribution guidelines.

**Acceptance Criteria:**
- [ ] CONTRIBUTING.md created
- [ ] Code style guide
- [ ] Git workflow documented
- [ ] PR template created

---

## Notes

### Prioritization Principles
1. **Foundation First:** Documentation and structure before code
2. **Feasibility Validation:** Prove technical approach works before building
3. **Core Learning Loop:** Get question → retrieval → explanation working end-to-end
4. **Content Quality:** Real Grade 6 content pack is critical for validation

### Agent Assignment Strategy
- Infrastructure Agent: Directory structure, tooling setup
- Documentation Agent: ADRs, architecture docs
- Research Agent: Technology evaluation
- ML Engineer Agent: Model integration, retrieval system
- Mobile Engineer Agent: Android app development
- Content Creator Agent: Educational content development
- Product Agent: UX design, preferences system

### Definition of Done
- Code reviewed and merged
- Tests written and passing
- Documentation updated
- Works on target Android devices (3GB RAM)
- No degradation in performance/battery

### Out of Scope for V1
- Voice interface
- Cloud features
- Teacher dashboards
- Multiple subjects beyond Grade 6 Math
- Advanced personalization beyond basic preferences
- Social/collaborative features
