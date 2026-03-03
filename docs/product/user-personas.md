# eZansiEdgeAI: User Personas

**Status:** Current  
**Last Updated:** 2026-02  
**Audience:** Contributors, Product Owners, UX, Content Authors

---

## 1. Purpose

These personas represent the real people eZansiEdgeAI is built for. Every design decision, feature prioritisation, and content choice should be evaluated through the lens of at least one of these personas.

---

## 2. Persona 1 — The Learner

**Name:** Siyanda  
**Age:** 12  
**Grade:** 6  
**Location:** Township adjacent to a secondary city, Eastern Cape

### Context
- Attends a public school with 40+ learners per class
- Has one phone in the household, shared with siblings — primarily uses it in evenings
- Home internet: none. Mobile data: limited prepaid, used carefully
- Power: load shedding affects her home 4–6 hours per day
- Most homework is done by candlelight or with a small solar lamp

### Goals
- Understand Maths concepts she missed in class or found confusing
- Get help with homework problems without having to wait for a teacher or parent
- Build confidence in a subject she finds difficult

### Frustrations
- Can't afford data to look up explanations online
- Parents can't help with Maths — they finished school at Grade 8
- Doesn't have a textbook at home — only access is at school during the day
- Some apps she's tried are too complicated or require internet

### What She Needs from eZansiEdgeAI
- Works on her shared Android phone with no internet required
- Answers that feel like a patient teacher explaining, not a textbook definition
- Fast enough not to drain the phone battery before she finishes homework
- Simple enough to use without asking anyone how it works
- Explanations matched to her reading level and learning pace

### Design Implications
- V1 text interface must be usable on a small screen (360–390dp width)
- Responses must be written at Grade 6 reading level — simple, clear, encouraging
- No login, no setup, no barriers between opening the app and getting help
- Offline operation is non-negotiable for this persona
- Explanation style must feel approachable — not like a formal textbook

---

## 3. Persona 2 — The Teacher

**Name:** Ms Nkosi  
**Age:** 38  
**Role:** Grade 6 Mathematics teacher  
**Location:** Rural school, KwaZulu-Natal

### Context
- Teaches 3 classes of Grade 6 (total ~120 learners)
- Has a personal Android phone; limited school computer access
- Digital literacy: comfortable with WhatsApp, basic apps; not comfortable with IT setup
- School has one partially-functional computer lab; school WiFi is inconsistent
- Has seen previous "tech initiatives" arrive and disappear without support

### Goals
- Find tools that genuinely help learners without requiring ongoing management
- Trust that the content being delivered to learners is accurate and curriculum-aligned
- Recommend something to learners' parents without complex setup instructions

### Frustrations
- Previous tools required email accounts, logins, or cloud setup — too many steps
- Tools that worked for a while then stopped working when subscriptions expired
- Anything that required her to be the IT support person
- Content that was "educational" but not CAPS-aligned and confused learners

### What She Needs from eZansiEdgeAI
- Can install the app on a learner's phone in under 5 minutes
- Confident that content is CAPS-aligned and correct
- No ongoing cost or maintenance burden
- Can recommend it to parents without needing to support them
- Does not require her to manage accounts, passwords, or device administration

### Design Implications
- Installation must be a single APK — no multi-step process
- Content accuracy and CAPS alignment must be clearly documented
- App must work on the range of phones learners actually own
- Teacher should be able to test the app herself before recommending it
- No "it stopped working" — reliability is essential for her trust

---

## 4. Persona 3 — The School Admin / NGO Partner

**Name:** Mr Dlamini  
**Age:** 52  
**Role:** School Principal / NGO Programme Manager  
**Location:** Semi-urban school cluster, Gauteng

### Context
- Oversees technology adoption decisions for the school or programme
- Accountable for outcomes — needs to justify investments of time and resource
- Frequently dealing with load shedding affecting school operations
- Limited IT budget; no dedicated IT staff
- Has existing relationships with NGOs providing devices or connectivity support

### Goals
- Deploy a learning support tool that continues to work when the lights go out
- Demonstrate value to parents, funders, and governing body
- Find something that doesn't require ongoing cost to sustain
- Protect learner privacy — reputational risk from data misuse is real

### Frustrations
- Tech tools with ongoing licence costs that aren't sustainable
- Tools that require cloud services and break when internet is down
- Data privacy concerns — tools that phone home with learner data
- Deployment complexity — needs outside specialist to install anything

### What They Need from eZansiEdgeAI
- Zero operational cost after initial deployment
- Continues working during load shedding (offline on phones)
- Can be deployed without IT specialist support
- Clear, honest privacy statement (local data only)
- Open source — can be inspected and trusted

### Design Implications
- Must be genuinely free — no hidden costs, no "freemium" traps
- Edge node must auto-recover from power outages without manual restart
- Privacy documentation must be prominent and plain-language
- Open source licence must be visible and understandable
- Deployment guide must be written for a non-technical administrator

---

## 5. Summary Table

| Dimension | Siyanda (Learner) | Ms Nkosi (Teacher) | Mr Dlamini (Admin/NGO) |
|-----------|-------------------|-------------------|----------------------|
| Primary need | Offline homework help | Easy install, accurate content | Zero cost, reliability |
| Tech literacy | Basic phone user | Basic apps, not IT | Management-level, not IT |
| Connectivity | None at home | Intermittent school WiFi | Aware of constraints |
| Key concern | Battery drain, complexity | Content accuracy, ongoing burden | Cost, privacy, load shedding |
| Trust signal | It works offline, no data needed | CAPS alignment, reliable | Open source, no recurring cost |

---

## 6. Related Documents

- [Product Vision](./vision.md)
- [Constraints](./constraints.md)
- [Success Metrics](./success-metrics.md)
