---
name: skill-methodology
description: "A rigorous 10-step methodology for creating expert-level Claude skills. Use when developing new skills that require deep domain expertise, when existing skills feel like 'instruction manuals' rather than expertise transfer, or when skills need systematic quality improvement. Implements the 4 Core Truths: Expertise Transfer (not instructions), Flow (not friction), Voice Matches Domain, and Focused Beats Comprehensive."
---

# Skill Development Methodology

## Philosophy: The 4 Core Truths

Every decision in skill creation filters through these principles:

| Truth | What It Means |
|-------|--------------|
| **Expertise Transfer, Not Instructions** | Make Claude *think* like an expert, not follow steps |
| **Flow, Not Friction** | Produce output, not intermediate documents |
| **Voice Matches Domain** | Sound like a practitioner, not documentation |
| **Focused Beats Comprehensive** | Constrain ruthlessly. Every section earns its place |

## The 10-Step Process

```
UNDERSTAND → EXPLORE → RESEARCH → SYNTHESIZE → DRAFT → SELF-CRITIQUE → ITERATE → TEST → FINALIZE
```

### Phase 1: Discovery (Steps 1-4)

Before writing a single line, understand the domain deeply.

#### Step 1: UNDERSTAND — What skill? What problem?

Define the skill's purpose with precision:

```markdown
## Skill Definition Worksheet

**Skill Name**: _______________
**One-sentence purpose**: What does an expert do that Claude cannot do unaided?
**Success looks like**: Describe the ideal output a user would receive
**Failure looks like**: What happens without this skill?
**Target user says**: "I need Claude to _______________"
```

#### Step 2: EXPLORE — See where Claude fails without guidance

**Critical step.** Actually test Claude without the skill:

1. Collect 5-10 representative tasks the skill should handle
2. Have Claude attempt each task with NO guidance
3. Document specific failures:
   - Wrong approach chosen?
   - Missing domain knowledge?
   - Poor output format?
   - Inefficient workflow?

Record failures in `worksheets/exploration-log.md`. These failures become your skill's requirements.

#### Step 3: RESEARCH — Go deep on the domain

Become the expert (or consult one):

- Read how practitioners actually work, not how they document their work
- Identify the tacit knowledge experts have but rarely articulate
- Find the decision points where novices go wrong
- Collect real examples of excellent output

Sources: practitioner blogs, conference talks, Stack Overflow debates, expert interviews, professional standards documents.

#### Step 4: SYNTHESIZE — Extract principles from research

Transform research into transferable expertise:

```markdown
## Synthesis Output

**Mental Model**: How does an expert think about this problem space?
**Key Decisions**: What are the 3-5 critical decision points?
**Common Mistakes**: What do novices get wrong?
**Quality Markers**: How do you recognize excellent output?
**Vocabulary**: What terms must Claude use correctly?
```

### Phase 2: Creation (Steps 5-6)

#### Step 5: DRAFT — Write initial skill

Use the template at `templates/SKILL-TEMPLATE.md`. Key principles:

**Expertise Transfer, Not Instructions**
```markdown
# BAD (Instructions)
1. First, analyze the input
2. Then, identify the key elements
3. Next, apply the transformation
4. Finally, format the output

# GOOD (Expertise Transfer)
Think like a senior [domain] professional reviewing this for the first time.
Your instinct is to [key behavior]. Watch for [common pitfall] which 
signals [underlying issue].
```

**Flow, Not Friction**
```markdown
# BAD (Friction)
Before proceeding, create a plan document outlining your approach.
Then create an analysis document. Then create your output.

# GOOD (Flow)
Produce the [output] directly. Internal reasoning happens silently.
```

**Voice Matches Domain**
```markdown
# BAD (Documentation voice)
The system shall process the input according to the specified parameters.

# GOOD (Practitioner voice)
When the data looks messy, trust the timestamps over the labels—
labels get copy-pasted wrong constantly.
```

**Focused Beats Comprehensive**

Before including any section, ask: "If I delete this, does the skill get worse?" If uncertain, delete it.

#### Step 6: SELF-CRITIQUE — Review against quality criteria

Run through the Quality Checklist (`references/quality-checklist.md`):

- [ ] Every section earns its place (could delete nothing)
- [ ] Sounds like an expert, not a manual
- [ ] Produces output directly, not intermediate artifacts
- [ ] Handles the failure cases from Step 2
- [ ] Under 500 lines in SKILL.md body
- [ ] No redundancy with Claude's base capabilities

### Phase 3: Refinement (Steps 7-9)

#### Step 7: ITERATE — Fix gaps, get feedback, improve

Systematic improvement cycle:

1. **Gap Analysis**: Compare skill against Step 2 failures. Does it address each one?
2. **Expert Review**: Have a domain expert read it. Does it match how they think?
3. **Compression Pass**: Remove 20% of content while preserving all value
4. **Voice Check**: Read aloud. Does it sound like a practitioner?

#### Step 8: TEST — Use skill on real scenarios

Execute the skill against your original test cases from Step 2:

```markdown
## Test Protocol

For each test case:
1. Use the skill exactly as written
2. Document: Did it produce expert-quality output?
3. If not: What went wrong? What's missing?
4. Update the skill based on findings
```

Test against edge cases practitioners would recognize but novices wouldn't anticipate.

#### Step 9: FINALIZE — Codify into optimal structure

Final structure optimization:

1. **Frontmatter**: Ensure description captures ALL trigger conditions
2. **Progressive Disclosure**: Core workflow in SKILL.md, details in references/
3. **Scripts**: Extract any repeated code into scripts/
4. **Assets**: Include templates/examples that get used in output

## Directory Structure

```
skill-name/
├── SKILL.md              # Core expertise (under 500 lines)
├── references/           # Deep details loaded on-demand
│   ├── examples.md       # Input/output pairs
│   └── edge-cases.md     # Non-obvious situations
├── scripts/              # Reusable code
└── assets/               # Templates, images, etc.
```

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead |
|--------------|--------------|---------|
| Comprehensive coverage | Bloats context, buries signal | Ruthlessly focus on what Claude doesn't know |
| Step-by-step instructions | Creates mechanical following, not expertise | Transfer mental models and decision frameworks |
| Generic voice | Sounds like documentation | Use domain-specific vocabulary and reasoning |
| Intermediate artifacts | Wastes tokens on process, not output | Go directly to deliverable |
| "Best practices" lists | Too abstract to apply | Concrete examples of good vs. bad |

## Quick Reference: The Core Questions

At every decision point, ask:

1. **Would an expert include this?** (Expertise Transfer)
2. **Does this produce output or process?** (Flow)
3. **Does this sound like a practitioner?** (Voice)
4. **Can I delete this without losing value?** (Focused)

If any answer is wrong, revise.
