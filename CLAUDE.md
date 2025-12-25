# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **skill development methodology template** for creating Claude Code skills. It implements the "4 Core Truths" philosophy for expertise transfer rather than mechanical instruction-following.

## The 4 Core Truths

Every skill created using this methodology must embody:

| Truth | Principle |
|-------|-----------|
| **Expertise Transfer > Instructions** | Make Claude *think* like an expert, not follow steps |
| **Flow > Friction** | Produce output directly, not intermediate documents |
| **Voice Matches Domain** | Sound like a practitioner, not documentation |
| **Focused > Comprehensive** | Every section earns its place. SKILL.md body under 500 lines |

## File Structure

```
README.md                   # Project overview and quick start
SKILL.md                    # Main skill definition (frontmatter + methodology)
templates/
  SKILL-TEMPLATE.md         # Template for creating new skills
worksheets/
  skill-definition.md       # Step 1: Define skill purpose
  exploration-log.md        # Step 2: Document Claude's failures
  synthesis-worksheet.md    # Step 4: Extract expertise principles
  test-protocol.md          # Step 8: Validate with real scenarios
references/
  quality-checklist.md      # Step 6: Self-critique against Core Truths
  anti-patterns.md          # Common mistakes and fixes
  transformation-examples.md # Before/after skill transformations
scripts/
  validate_skill.py         # Validation script
```

## The 10-Step Process

```
UNDERSTAND → EXPLORE → RESEARCH → SYNTHESIZE → DRAFT → SELF-CRITIQUE → ITERATE → TEST → FINALIZE
```

**Phase 1 - Discovery**: Define skill → Test Claude's failures → Research domain → Synthesize expertise
**Phase 2 - Creation**: Draft using template → Self-critique against Core Truths
**Phase 3 - Refinement**: Iterate based on gaps → Test with real scenarios → Finalize structure

## Creating a New Skill

1. Copy `templates/SKILL-TEMPLATE.md` to your skill's directory
2. Complete worksheets in order: `worksheets/skill-definition.md` → `worksheets/exploration-log.md` → `worksheets/synthesis-worksheet.md`
3. Draft skill following template guidance (delete HTML comments after)
4. Run through `references/quality-checklist.md` before testing
5. Test using `worksheets/test-protocol.md` with cases from exploration
6. Validate with `python scripts/validate_skill.py path/to/SKILL.md`

## Key Anti-Patterns to Avoid

- **User Manual**: Step-by-step instructions instead of mental models
- **Encyclopedia**: Comprehensive coverage that bloats context
- **Checkbox Lists**: Mechanical validation instead of expert judgment
- **Process Doc**: Intermediate artifacts before output
- **Generic Best Practices**: "Be thorough" adds nothing

## Core Questions at Every Decision Point

1. Would an expert include this?
2. Does this produce output or process?
3. Does this sound like a practitioner?
4. Can I delete this without losing value?
