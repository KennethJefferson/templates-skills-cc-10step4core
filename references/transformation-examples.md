# Transformation Examples

Side-by-side comparisons showing how to transform instruction-style skills into expertise-transfer skills.

## Example 1: Code Review Skill

### BEFORE (Instruction Style)

```markdown
---
name: code-review
description: Reviews code for issues
---

# Code Review Skill

## Steps
1. First, read through the code
2. Check for syntax errors
3. Look for security issues
4. Check for performance problems
5. Review code style
6. Write your feedback
7. Prioritize issues

## Checklist
- [ ] Syntax correct
- [ ] No security issues
- [ ] Performance acceptable
- [ ] Style consistent
- [ ] Tests present
```

**Problems:**
- Reads like a manual
- No expertise transfer
- Generic advice Claude already knows
- Checklist doesn't capture expert judgment

### AFTER (Expertise Transfer)

```markdown
---
name: code-review
description: "Expert code review with security focus. Use when reviewing PRs, auditing code for vulnerabilities, or providing feedback on code quality. Focuses on what experienced reviewers catch that static analysis misses."
---

# Code Review

## Mental Model

Review like a senior engineer who's been burned before. Your instinct is to 
trace data flow—where does untrusted input enter, and what can it touch? 
Don't trust function names; read what the code actually does.

## What Experts Notice First

| Signal | What It Means | Action |
|--------|---------------|--------|
| Complex auth logic | Usually wrong somewhere | Trace every path manually |
| String concatenation with user input | Injection risk | Flag immediately |
| Catch-all exception handlers | Bugs hiding | Ask what's being swallowed |
| Comments explaining "why" removed | Tribal knowledge lost | Ask for context |

## Quality Markers

Strong review: Identifies non-obvious issues, explains the "why," suggests 
concrete fixes, prioritizes by actual risk.

Weak review: Lists superficial style issues, misses the real bugs, 
doesn't understand the business context.

## Practitioner Wisdom

"The scariest code is the code that looks fine. Obvious bugs get fixed; 
subtle bugs ship."

"When reviewing auth, assume the attacker has read the code. What would 
they try?"
```

---

## Example 2: Data Analysis Skill

### BEFORE (Instruction Style)

```markdown
---
name: data-analysis
description: Analyzes data
---

# Data Analysis

## Process
1. Load the data
2. Clean the data
3. Explore the data
4. Create visualizations
5. Draw conclusions
6. Present findings

## Best Practices
- Check for missing values
- Handle outliers
- Use appropriate charts
- Document assumptions
```

**Problems:**
- Generic process Claude already knows
- No domain expertise
- "Best practices" too vague
- No judgment transfer

### AFTER (Expertise Transfer)

```markdown
---
name: data-analysis
description: "Rigorous data analysis focusing on insights over process. Use for exploratory analysis, finding patterns in datasets, or validating hypotheses with data."
---

# Data Analysis

## Mental Model

Think like a detective who's skeptical of everything. Data lies—through 
collection bias, survivorship bias, confounders, or just bad encoding. 
Your job is to find truth despite the data's attempts to mislead you.

## Decision Framework

| When You See... | Expert Response |
|-----------------|-----------------|
| Perfect correlation | Suspect data leakage or tautology first |
| Counterintuitive result | More likely you're right than the common wisdom is |
| Missing data patterns | This IS the finding—why is it missing? |
| Outliers | Understand before removing—sometimes they're the story |

## What Separates Good Analysis

**Strong analysis asks**: "What would have to be true for this conclusion 
to be wrong?"

**Weak analysis asks**: "How can I prove what I already believe?"

## Expert Shortcuts

- Plot before modeling. Always. Your eyes catch things statistics miss.
- When correlations vanish after controlling for Z, Z is your real story.
- Small p-value, small effect size = statistically significant, practically useless.
```

---

## The Transformation Process

### Step 1: Delete Generic Advice
Remove anything Claude already knows. "Check for errors" adds nothing.

### Step 2: Add Expert Judgment
Replace "what to do" with "how to think" and "what to notice."

### Step 3: Include Non-Obvious Insights
What do experts know that isn't written down anywhere?

### Step 4: Use Practitioner Voice
Write like you're explaining to a competent peer, not documenting for a novice.

### Step 5: Show Don't Tell
Decision tables and examples beat abstract principles.
