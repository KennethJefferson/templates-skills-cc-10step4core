# Anti-Patterns Reference

Common mistakes in skill creation and how to fix them.

## Anti-Pattern 1: The User Manual

**Symptom**: Skill reads like software documentation.

**Example (BAD)**:
```markdown
## Usage
1. First, input your data
2. The system will process the input
3. Review the output
4. Make corrections as needed
5. Finalize the result
```

**Why it fails**: Claude follows steps mechanically without understanding. No expertise transfer occurs.

**Fix (GOOD)**:
```markdown
## Mental Model
Approach this like a senior analyst who's reviewed thousands of these. 
Your first instinct is to check for [specific signal]—if it's off, 
everything downstream is suspect. Trust patterns over labels; labels 
lie, patterns don't.
```

---

## Anti-Pattern 2: The Encyclopedia

**Symptom**: Comprehensive coverage of everything related to the topic.

**Example (BAD)**:
```markdown
## Background
[500 words of context]

## History  
[300 words of history]

## Related Concepts
[400 words of tangential information]

## The Actual Workflow
[Finally, buried at line 300]
```

**Why it fails**: Bloats context, buries signal in noise, wastes tokens on things Claude already knows.

**Fix (GOOD)**:
```markdown
## Core Workflow
[The essential 50 lines]

For deep background, see references/context.md
```

---

## Anti-Pattern 3: The Checkbox List

**Symptom**: Quality defined as completing a checklist.

**Example (BAD)**:
```markdown
## Validation Checklist
- [ ] Has title
- [ ] Has introduction
- [ ] Has body
- [ ] Has conclusion
- [ ] Under word limit
- [ ] No spelling errors
```

**Why it fails**: Mechanical compliance ≠ quality. An expert doesn't validate by checklist.

**Fix (GOOD)**:
```markdown
## Quality Markers
Strong output has: clear thesis visible in first paragraph, evidence 
that anticipates counterarguments, conclusion that advances beyond 
introduction.

Weak output feels: defensive, hedged, or states the obvious.
```

---

## Anti-Pattern 4: The Process Doc

**Symptom**: More process than output.

**Example (BAD)**:
```markdown
## Workflow
1. Create analysis plan
2. Document assumptions  
3. Build analysis framework
4. Execute analysis
5. Document findings
6. Create summary document
7. Review summary
8. Finalize output
```

**Why it fails**: User gets 7 intermediate artifacts before getting what they actually wanted.

**Fix (GOOD)**:
```markdown
## Workflow
Produce the analysis directly. Structure output as: [format].
```

---

## Anti-Pattern 5: The Hedged Advice

**Symptom**: Every statement qualified into uselessness.

**Example (BAD)**:
```markdown
You might want to consider potentially checking whether it could be 
helpful to perhaps verify that the data may or may not be valid, 
depending on the circumstances.
```

**Why it fails**: No actual guidance provided. Experts have opinions.

**Fix (GOOD)**:
```markdown
Check the timestamps first. If they're inconsistent, stop—garbage in, 
garbage out. Don't trust user-provided labels until you've verified 
against the raw data.
```

---

## Anti-Pattern 6: The Generic Best Practices

**Symptom**: Advice that applies to everything and therefore nothing.

**Example (BAD)**:
```markdown
## Best Practices
- Be thorough
- Check your work
- Consider edge cases
- Follow standards
- Document your process
```

**Why it fails**: Too vague to apply. Claude already knows these.

**Fix (GOOD)**:
```markdown
## What Experts Watch For
In [this specific domain], the failure mode is usually [specific thing]. 
Check [specific location] for [specific pattern]. If you see [specific 
signal], it means [specific diagnosis].
```

---

## Anti-Pattern 7: The Documentation Voice

**Symptom**: Sounds like technical writing, not a practitioner.

**Example (BAD)**:
```markdown
The system shall validate inputs prior to processing. Invalid inputs 
shall result in an error response. The response format shall conform 
to the specification defined in Section 4.2.
```

**Why it fails**: No expertise transfer. Could be written by someone who's never done the work.

**Fix (GOOD)**:
```markdown
Validate inputs before touching anything else—I've been burned by 
invalid data propagating through the whole pipeline. When something 
looks off, it usually is.
```

---

## Quick Detection

**Ask yourself**: 

1. Could this have been written by someone who's never actually done this work?
2. Could Claude follow this without understanding anything?
3. Does this produce output or process?
4. Would an expert cringe reading this?

If any answer is concerning, you have an anti-pattern.
