#!/usr/bin/env python3
"""
Skill Quality Validator

Validates a skill against the 4 Core Truths:
1. Expertise Transfer, Not Instructions
2. Flow, Not Friction  
3. Voice Matches Domain
4. Focused Beats Comprehensive

Usage:
    python validate_skill.py <path-to-skill-folder>
"""

import sys
import os
import re
import yaml
from pathlib import Path

class SkillValidator:
    def __init__(self, skill_path):
        self.skill_path = Path(skill_path)
        self.skill_md_path = self.skill_path / "SKILL.md"
        self.issues = []
        self.warnings = []
        self.content = ""
        self.frontmatter = {}
        self.body = ""
        
    def validate(self):
        """Run all validations and return results."""
        if not self.skill_md_path.exists():
            self.issues.append("CRITICAL: SKILL.md not found")
            return self._results()
            
        self._load_skill()
        
        # Structure checks
        self._check_frontmatter()
        self._check_line_count()
        self._check_no_readme()
        
        # Core Truth checks
        self._check_expertise_transfer()
        self._check_flow_not_friction()
        self._check_voice()
        self._check_focus()
        
        return self._results()
    
    def _load_skill(self):
        """Load and parse SKILL.md content."""
        self.content = self.skill_md_path.read_text()
        
        # Parse frontmatter
        if self.content.startswith('---'):
            parts = self.content.split('---', 2)
            if len(parts) >= 3:
                try:
                    self.frontmatter = yaml.safe_load(parts[1])
                    self.body = parts[2]
                except:
                    self.issues.append("CRITICAL: Invalid YAML frontmatter")
        else:
            self.issues.append("CRITICAL: Missing frontmatter")
            self.body = self.content
            
    def _check_frontmatter(self):
        """Validate frontmatter structure."""
        if not self.frontmatter:
            return
            
        if 'name' not in self.frontmatter:
            self.issues.append("CRITICAL: Missing 'name' in frontmatter")
            
        if 'description' not in self.frontmatter:
            self.issues.append("CRITICAL: Missing 'description' in frontmatter")
        else:
            desc = self.frontmatter['description']
            if len(desc) < 50:
                self.warnings.append("Description seems too short (< 50 chars)")
            if 'when' not in desc.lower() and 'use' not in desc.lower():
                self.warnings.append("Description may be missing trigger conditions")
                
    def _check_line_count(self):
        """Check if body is under 500 lines."""
        lines = self.body.strip().split('\n')
        if len(lines) > 500:
            self.issues.append(f"FOCUS: Body is {len(lines)} lines (should be < 500)")
        elif len(lines) > 400:
            self.warnings.append(f"Body is {len(lines)} lines - approaching 500 limit")
            
    def _check_no_readme(self):
        """Check for auxiliary documentation files."""
        bad_files = ['README.md', 'CHANGELOG.md', 'INSTALLATION.md', 'QUICK_REFERENCE.md']
        for bad_file in bad_files:
            if (self.skill_path / bad_file).exists():
                self.issues.append(f"FOCUS: Remove {bad_file} - skills shouldn't have auxiliary docs")
                
    def _check_expertise_transfer(self):
        """Check for instruction-style patterns (anti-pattern)."""
        # Check for numbered step patterns
        step_pattern = r'^\s*\d+\.\s*(First|Then|Next|Finally|After that)'
        matches = re.findall(step_pattern, self.body, re.MULTILINE | re.IGNORECASE)
        if len(matches) > 2:
            self.warnings.append(
                f"EXPERTISE: Found {len(matches)} sequential step indicators "
                f"(First/Then/Next/Finally) - consider transferring mental models instead"
            )
            
        # Check for mechanical language
        mechanical = ['the system will', 'the system shall', 'shall be', 'must be performed']
        for phrase in mechanical:
            if phrase in self.body.lower():
                self.warnings.append(f"EXPERTISE: Found '{phrase}' - sounds like documentation, not expertise")
                
    def _check_flow_not_friction(self):
        """Check for intermediate artifact requirements."""
        friction_phrases = [
            'create a plan',
            'planning document', 
            'analysis document',
            'document your',
            'create an outline',
            'before proceeding',
            'intermediate'
        ]
        for phrase in friction_phrases:
            if phrase in self.body.lower():
                self.warnings.append(f"FLOW: Found '{phrase}' - may introduce unnecessary friction")
                
    def _check_voice(self):
        """Check for non-practitioner voice."""
        # Check for overly formal language
        formal = ['shall', 'whereas', 'hereby', 'aforementioned', 'pursuant to']
        found_formal = [f for f in formal if f in self.body.lower()]
        if found_formal:
            self.warnings.append(f"VOICE: Overly formal language found: {found_formal}")
            
        # Check for passive voice overuse (simple heuristic)
        passive = len(re.findall(r'\b(is|are|was|were|be|been|being)\s+\w+ed\b', self.body))
        if passive > 10:
            self.warnings.append(f"VOICE: High passive voice count ({passive}) - consider more active voice")
            
    def _check_focus(self):
        """Check for unfocused content."""
        # Check for generic section headers
        generic_headers = ['overview', 'introduction', 'background', 'prerequisites', 'best practices']
        body_lower = self.body.lower()
        for header in generic_headers:
            if f'## {header}' in body_lower or f'# {header}' in body_lower:
                self.warnings.append(f"FOCUS: Section '{header}' may be unfocused - consider if necessary")
                
        # Check for "When to use" in body (should be in description)
        if 'when to use' in body_lower:
            self.warnings.append("FOCUS: 'When to use' belongs in frontmatter description, not body")
            
    def _results(self):
        """Format and return results."""
        return {
            'valid': len(self.issues) == 0,
            'issues': self.issues,
            'warnings': self.warnings,
            'stats': {
                'body_lines': len(self.body.strip().split('\n')) if self.body else 0,
                'has_references': (self.skill_path / 'references').exists(),
                'has_scripts': (self.skill_path / 'scripts').exists(),
                'has_assets': (self.skill_path / 'assets').exists(),
            }
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <path-to-skill-folder>")
        sys.exit(1)
        
    skill_path = sys.argv[1]
    
    if not os.path.isdir(skill_path):
        print(f"Error: {skill_path} is not a directory")
        sys.exit(1)
        
    validator = SkillValidator(skill_path)
    results = validator.validate()
    
    print("\n" + "="*60)
    print("SKILL VALIDATION REPORT")
    print("="*60)
    print(f"\nSkill: {skill_path}")
    print(f"Status: {'✓ VALID' if results['valid'] else '✗ INVALID'}")
    
    print(f"\nStats:")
    print(f"  Body lines: {results['stats']['body_lines']}")
    print(f"  Has references/: {results['stats']['has_references']}")
    print(f"  Has scripts/: {results['stats']['has_scripts']}")
    print(f"  Has assets/: {results['stats']['has_assets']}")
    
    if results['issues']:
        print(f"\n❌ ISSUES ({len(results['issues'])}):")
        for issue in results['issues']:
            print(f"  • {issue}")
            
    if results['warnings']:
        print(f"\n⚠️  WARNINGS ({len(results['warnings'])}):")
        for warning in results['warnings']:
            print(f"  • {warning}")
            
    if not results['issues'] and not results['warnings']:
        print("\n✨ No issues or warnings found!")
        
    print("\n" + "="*60)
    
    sys.exit(0 if results['valid'] else 1)


if __name__ == "__main__":
    main()
