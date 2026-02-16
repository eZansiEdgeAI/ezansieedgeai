#!/usr/bin/env python3
"""
PR Constitution Generator

Generates a PR validation constitution based on the project vision.
This ensures PR validation is aligned with whatever vision is supplied,
not hardcoded to a specific domain (like education).
"""

import os
import sys
import yaml
import re
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

# Add parent directory to path to import master_agent
sys.path.insert(0, str(Path(__file__).parent))

try:
    from master_agent import MasterAgent
except ImportError:
    # Try alternative import
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "master_agent",
        Path(__file__).parent / "master-agent.py"
    )
    master_agent_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(master_agent_module)
    MasterAgent = master_agent_module.MasterAgent


class PRConstitutionGenerator:
    """
    Generates PR validation constitution from project vision.
    """
    
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.master_agent = MasterAgent(repo_root)
        self.vision_data = None
        self.constitution = None
    
    def generate(self, output_path: str = None) -> Dict[str, Any]:
        """
        Generate PR constitution from vision.
        
        Args:
            output_path: Optional path to save the constitution YAML
            
        Returns:
            Dictionary containing the PR constitution
        """
        # Step 1: Interpret vision
        print("📖 Interpreting project vision...")
        self.vision_data = self.master_agent.interpret_vision()
        print(f"   ✓ Vision found: {self.master_agent.vision_path}")
        print(f"   ✓ Domain: {self.vision_data['domain']}")
        
        # Step 2: Generate base constitution
        print("\n📜 Generating constitution from vision...")
        base_constitution = self.master_agent.generate_constitution()
        
        # Step 3: Create PR-specific constitution
        print("\n🔍 Creating PR validation rules...")
        pr_constitution = self._create_pr_constitution(base_constitution)
        
        # Step 4: Save if output path provided
        if output_path:
            self._save_constitution(pr_constitution, output_path)
            print(f"\n💾 Constitution saved to: {output_path}")
        
        self.constitution = pr_constitution
        return pr_constitution
    
    def _create_pr_constitution(self, base_constitution: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create PR-specific constitution from base constitution.
        """
        pr_constitution = {
            'version': '1.0',
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'generated_from': str(self.master_agent.vision_path),
            'domain': self.vision_data['domain'],
            
            # Core principles derived from vision
            'core_principles': self._derive_core_principles(),
            
            # Technical requirements based on vision constraints
            'technical_requirements': self._derive_technical_requirements(),
            
            # Code quality requirements (generic)
            'code_quality': self._define_code_quality_requirements(),
            
            # Security requirements (generic but domain-aware)
            'security': self._define_security_requirements(),
            
            # Architecture alignment based on vision
            'architecture': self._derive_architecture_requirements(),
            
            # Breaking changes policy
            'breaking_changes': self._define_breaking_changes_policy(),
            
            # Enforcement levels
            'enforcement_levels': self._define_enforcement_levels(),
            
            # Review process
            'review_process': self._define_review_process(),
            
            # Exception process
            'exceptions': self._define_exception_process(),
            
            # Metrics
            'metrics': self._define_metrics()
        }
        
        return pr_constitution
    
    def _derive_core_principles(self) -> Dict[str, Any]:
        """
        Derive core principles from vision principles and values.
        """
        principles = {}
        vision_principles = self.vision_data.get('principles', [])
        vision_values = self.vision_data.get('values', [])
        
        # Add principles from vision (these are the main ones)
        for i, principle in enumerate(vision_principles[:7]):  # Top 7 principles
            # Extract principle name (before colon if present)
            principle_name = principle.split(':')[0].strip()
            principle_desc = principle
            
            principle_id = principle_name.lower().replace(' ', '_').replace('-', '_')
            # Clean up ID
            principle_id = ''.join(c for c in principle_id if c.isalnum() or c == '_')[:40]
            
            principles[principle_id] = {
                'description': principle_desc,
                'enforcement': 'mandatory',
                'checks': self._generate_principle_checks(principle_desc)
            }
        
        # Only add values if we don't have enough principles
        if len(principles) < 3:
            for value in vision_values[:3]:
                value_id = f"{value}_focused"
                if value_id not in principles:
                    principles[value_id] = {
                        'description': f"Maintain {value} as a core value",
                        'enforcement': 'mandatory',
                        'checks': self._generate_value_checks(value)
                    }
        
        return principles
    
    def _generate_principle_checks(self, principle: str) -> List[str]:
        """
        Generate validation checks for a principle.
        """
        principle_lower = principle.lower()
        checks = []
        
        # Generic check - always include
        checks.append(f"Implementation aligns with principle")
        
        # Specific checks based on keywords
        if any(keyword in principle_lower for keyword in ['offline', 'connectivity', 'network']):
            checks.extend([
                "Feature works without network connectivity",
                "Graceful handling of network failures"
            ])
        elif any(keyword in principle_lower for keyword in ['mobile', 'phone', 'device']):
            checks.extend([
                "Mobile-friendly implementation",
                "Works on target mobile devices"
            ])
        elif any(keyword in principle_lower for keyword in ['simple', 'simplicity', 'easy']):
            checks.extend([
                "Solution is as simple as possible",
                "No unnecessary complexity"
            ])
        elif any(keyword in principle_lower for keyword in ['secure', 'security', 'privacy', 'protected']):
            checks.extend([
                "Security best practices followed",
                "No known vulnerabilities"
            ])
        elif any(keyword in principle_lower for keyword in ['performance', 'fast', 'speed', 'quick']):
            checks.extend([
                "Performance targets met",
                "No performance regressions"
            ])
        elif any(keyword in principle_lower for keyword in ['reliable', 'reliability', 'consistent', 'resilient']):
            checks.extend([
                "Error handling implemented",
                "Graceful degradation in edge cases"
            ])
        elif any(keyword in principle_lower for keyword in ['accessible', 'accessibility', 'anyone', 'anywhere']):
            checks.extend([
                "Works in target environments",
                "No unnecessary barriers"
            ])
        elif any(keyword in principle_lower for keyword in ['open', 'transparent', 'interoperable']):
            checks.extend([
                "Uses open standards where applicable",
                "Documented interfaces"
            ])
        else:
            # Default checks for unrecognized principles
            checks.extend([
                "Principle considered in design",
                "No violations of principle"
            ])
        
        return checks[:4]  # Max 4 checks per principle
    
    def _generate_value_checks(self, value: str) -> List[str]:
        """
        Generate checks for a value.
        """
        return [
            f"Implementation maintains {value}",
            f"No compromise on {value}",
            f"{value.capitalize()} validated in tests"
        ]
    
    def _derive_technical_requirements(self) -> Dict[str, Any]:
        """
        Derive technical requirements from vision constraints.
        """
        requirements = {}
        constraints = self.vision_data.get('constraints', [])
        domain = self.vision_data.get('domain')
        
        # Device compatibility (if mobile/device mentioned)
        arch_hints = ' '.join(self.vision_data.get('architecture_hints', [])).lower()
        if 'mobile' in arch_hints or 'phone' in arch_hints or 'device' in arch_hints:
            requirements['device_compatibility'] = {
                'description': 'Ensure compatibility with target devices',
                'checks': [
                    "Tested on target devices or emulators",
                    "Performance within acceptable range",
                    "No crashes on target platforms",
                    "Resource usage acceptable"
                ]
            }
        
        # Performance requirements
        if 'performance' in ' '.join(constraints).lower() or 'fast' in ' '.join(self.vision_data.get('values', [])):
            requirements['performance'] = {
                'description': 'Meet performance requirements',
                'checks': [
                    "Performance benchmarks run",
                    "No performance regressions",
                    "Response times acceptable",
                    "Resource usage optimized"
                ]
            }
        
        # Storage/resource constraints
        if any('storage' in c.lower() or 'memory' in c.lower() or 'resource' in c.lower() for c in constraints):
            requirements['resource_constraints'] = {
                'description': 'Respect resource constraints',
                'checks': [
                    "Storage impact documented",
                    "Memory usage acceptable",
                    "Resource cleanup implemented",
                    "Efficient data structures used"
                ]
            }
        
        return requirements
    
    def _define_code_quality_requirements(self) -> Dict[str, Any]:
        """
        Define generic code quality requirements.
        """
        return {
            'testing': {
                'requirements': {
                    'unit_tests': 'Required for new code',
                    'integration_tests': 'Required for key workflows',
                    'coverage': 'Maintain or improve'
                },
                'checks': [
                    "Tests written and passing",
                    "Coverage requirements met",
                    "Key scenarios tested",
                    "Tests are maintainable"
                ]
            },
            'documentation': {
                'required': [
                    "Code comments for complex logic",
                    "API documentation for public interfaces",
                    "README updates if needed",
                    "ADR for architectural decisions"
                ],
                'checks': [
                    "Documentation updated",
                    "Changes explained in PR",
                    "Examples provided where helpful",
                    "Breaking changes documented"
                ]
            },
            'code_style': {
                'requirements': [
                    "Follows project conventions",
                    "Linter passes",
                    "Consistent formatting",
                    "Meaningful names"
                ],
                'checks': [
                    "Linter passes",
                    "Style guide followed",
                    "No warnings introduced",
                    "Code review approved"
                ]
            }
        }
    
    def _define_security_requirements(self) -> Dict[str, Any]:
        """
        Define security requirements.
        """
        security_focused = 'secure' in self.vision_data.get('values', [])
        privacy_focused = 'private' in self.vision_data.get('values', [])
        
        requirements = {
            'data_protection': {
                'requirements': [
                    "Sensitive data encrypted at rest",
                    "Secure communication (HTTPS)",
                    "Input validation present",
                    "No hardcoded secrets"
                ],
                'checks': [
                    "Security scan passes",
                    "No known vulnerabilities",
                    "Secrets properly managed",
                    "Input sanitized"
                ]
            }
        }
        
        if privacy_focused:
            requirements['privacy'] = {
                'requirements': [
                    "Minimal data collection",
                    "User consent obtained",
                    "Data anonymized where possible",
                    "Privacy policy compliance"
                ],
                'checks': [
                    "Privacy review done",
                    "PII handled correctly",
                    "Consent flow appropriate",
                    "Audit trail in place"
                ]
            }
        
        return requirements
    
    def _derive_architecture_requirements(self) -> Dict[str, Any]:
        """
        Derive architecture requirements from vision.
        """
        return {
            'vision_compliance': {
                'description': 'Changes must align with project vision',
                'checks': [
                    "Aligns with stated mission",
                    "Follows vision principles",
                    "Supports vision goals",
                    "No conflicts with vision constraints"
                ]
            },
            'pattern_consistency': {
                'description': 'Follow established code patterns',
                'checks': [
                    "Uses existing patterns where applicable",
                    "New patterns justified and documented",
                    "Consistent with architecture",
                    "No architectural violations"
                ]
            }
        }
    
    def _define_breaking_changes_policy(self) -> Dict[str, Any]:
        """
        Define breaking changes policy.
        """
        return {
            'allowed': True,
            'conditions': [
                "Clearly documented",
                "Migration path provided",
                "Justified by significant benefit",
                "Approved by maintainers"
            ],
            'required_docs': [
                "BREAKING CHANGE tag in commit",
                "Migration guide",
                "Deprecation timeline",
                "Backward compatibility plan if possible"
            ]
        }
    
    def _define_enforcement_levels(self) -> Dict[str, Any]:
        """
        Define enforcement levels.
        """
        return {
            'critical': {
                'description': 'Must pass, no exceptions',
                'applies_to': [
                    'core_principles',
                    'security'
                ],
                'action': 'Block merge'
            },
            'required': {
                'description': 'Must pass or have approved exception',
                'applies_to': [
                    'technical_requirements',
                    'code_quality (testing, documentation)',
                    'architecture'
                ],
                'action': 'Block merge or require approval'
            },
            'recommended': {
                'description': 'Should pass, exceptions allowed with justification',
                'applies_to': [
                    'code_style (minor issues)',
                    'performance (context-dependent)'
                ],
                'action': 'Warning, require justification'
            }
        }
    
    def _define_review_process(self) -> Dict[str, Any]:
        """
        Define review process.
        """
        return {
            'automated_checks': [
                "Linter",
                "Unit tests",
                "Security scan",
                "Coverage check",
                "Build verification"
            ],
            'enforcement_agents': {
                'constitutional_judge': {
                    'checks': 'core_principles',
                    'authority': 'Block merge'
                },
                'security_enforcement': {
                    'checks': 'security',
                    'authority': 'Block merge'
                },
                'quality_enforcement': {
                    'checks': 'code_quality',
                    'authority': 'Request changes'
                }
            },
            'human_review': {
                'required_for': [
                    "Architectural changes",
                    "Breaking changes",
                    "Security-sensitive changes",
                    "New dependencies"
                ],
                'reviewers': 'Maintainers',
                'approval_count': 1
            }
        }
    
    def _define_exception_process(self) -> Dict[str, Any]:
        """
        Define exception process.
        """
        return {
            'allowed': True,
            'process': [
                "Document reason for exception",
                "Propose alternative compliance",
                "Get approval from maintainer",
                "Create issue to address properly"
            ],
            'documentation': [
                "Exception noted in PR",
                "Follow-up issue created",
                "Timeline for proper fix",
                "Risk assessment"
            ]
        }
    
    def _define_metrics(self) -> Dict[str, Any]:
        """
        Define metrics to track.
        """
        return {
            'tracked': [
                "First-time approval rate",
                "Common failure reasons",
                "Time to merge",
                "Rework frequency"
            ],
            'reporting': [
                "Weekly summary",
                "Trend analysis",
                "Process improvements"
            ]
        }
    
    def _save_constitution(self, constitution: Dict[str, Any], output_path: str):
        """
        Save constitution to YAML file.
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            f.write("# PR Merge Constitution\n")
            f.write("# This document was automatically generated from the project vision.\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Source: {constitution['generated_from']}\n\n")
            yaml.dump(constitution, f, default_flow_style=False, sort_keys=False, indent=2)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate PR validation constitution from project vision'
    )
    parser.add_argument(
        '--repo-root',
        help='Repository root directory (default: current directory)',
        default=None
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path (default: .github/agents/pr-merge-constitution.yaml)',
        default='.github/agents/pr-merge-constitution.yaml'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Generate but do not save to file'
    )
    
    args = parser.parse_args()
    
    try:
        generator = PRConstitutionGenerator(repo_root=args.repo_root)
        output_path = None if args.dry_run else args.output
        
        constitution = generator.generate(output_path=output_path)
        
        if args.dry_run:
            print("\n📋 Generated Constitution (dry-run):")
            print(yaml.dump(constitution, default_flow_style=False, sort_keys=False, indent=2))
        else:
            print("\n✅ PR Constitution generated successfully!")
            print(f"\n📦 Next steps:")
            print("   1. Review the generated constitution")
            print("   2. Customize if needed")
            print("   3. Run PR validation workflow")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
