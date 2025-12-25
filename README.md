# Claude Code Skills - 4 Core Truths Methodology

A rigorous methodology for creating expert-level Claude Code skills that transfer expertise rather than instructions.

## The Problem

Most skills read like user manuals—step-by-step instructions that Claude follows mechanically. The result: output that's technically correct but lacks expert judgment.

## The Solution: 4 Core Truths

Every skill created with this methodology embodies these principles:

| Truth | What It Means |
|-------|---------------|
| **Expertise Transfer > Instructions** | Make Claude *think* like an expert, not follow steps |
| **Flow > Friction** | Produce output directly, not intermediate documents |
| **Voice Matches Domain** | Sound like a practitioner, not documentation |
| **Focused > Comprehensive** | Every section earns its place |

## Quick Start

1. **Define** your skill using `worksheets/skill-definition.md`
2. **Explore** Claude's failures without guidance using `worksheets/exploration-log.md`
3. **Research** the domain deeply—how do practitioners actually think?
4. **Synthesize** expertise using `worksheets/synthesis-worksheet.md`
5. **Draft** using `templates/SKILL-TEMPLATE.md`
6. **Critique** against `references/quality-checklist.md`
7. **Test** with `worksheets/test-protocol.md`
8. **Validate** with `python scripts/validate_skill.py path/to/SKILL.md`

## The 10-Step Process

```
UNDERSTAND → EXPLORE → RESEARCH → SYNTHESIZE → DRAFT
                                                 ↓
                           FINALIZE ← TEST ← ITERATE ← SELF-CRITIQUE
```

**Phase 1 - Discovery** (Steps 1-4): Understand the domain before writing anything
**Phase 2 - Creation** (Steps 5-6): Draft and self-critique
**Phase 3 - Refinement** (Steps 7-9): Iterate, test, finalize

## Directory Structure

```
├── SKILL.md                 # The methodology itself (use as reference)
├── templates/
│   └── SKILL-TEMPLATE.md    # Start here when creating a new skill
├── worksheets/
│   ├── skill-definition.md  # Step 1: Define purpose
│   ├── exploration-log.md   # Step 2: Document failures
│   ├── synthesis-worksheet.md # Step 4: Extract principles
│   └── test-protocol.md     # Step 8: Validate
├── references/
│   ├── quality-checklist.md # Step 6: Self-critique
│   ├── anti-patterns.md     # Common mistakes
│   └── transformation-examples.md # Before/after examples
└── scripts/
    └── validate_skill.py    # Automated validation
```

## What Good Looks Like

**Bad (Instructions):**
```markdown
## Steps
1. First, analyze the input
2. Then, identify key elements
3. Next, apply the transformation
4. Finally, format the output
```

**Good (Expertise Transfer):**
```markdown
## Mental Model
Think like a senior analyst who's been burned before. Your first instinct
is to check [key signal]—if it's off, everything downstream is suspect.
Trust patterns over labels; labels lie, patterns don't.
```

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| User Manual | Mechanical following, no expertise |
| Encyclopedia | Bloats context, buries signal |
| Checkbox Lists | Compliance ≠ quality |
| Process Docs | Intermediate artifacts before output |
| Generic Best Practices | Too vague to apply |

## The Core Questions

At every decision point, ask:

1. **Would an expert include this?**
2. **Does this produce output or process?**
3. **Does this sound like a practitioner?**
4. **Can I delete this without losing value?**

If any answer is wrong, revise.

## License

MIT
