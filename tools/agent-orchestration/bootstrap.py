#!/usr/bin/env python3
"""
MaSf-vision Bootstrap Tool

This CLI tool helps users bootstrap the MaSf-vision framework into their own repositories.
It sets up the necessary files, generates the constitution, and configures workflows.
"""

import os
import sys
import argparse
import shutil
from pathlib import Path
from typing import Optional


class MaSfBootstrap:
    """
    Bootstrap the MaSf-vision framework into a repository.
    """
    
    def __init__(self, target_repo: str = None):
        self.target_repo = Path(target_repo) if target_repo else Path.cwd()
        self.framework_root = Path(__file__).parent.parent.parent  # Go up to repo root
    
    def bootstrap(self, options: dict) -> bool:
        """
        Main bootstrap process.
        
        Args:
            options: Dictionary of bootstrap options
            
        Returns:
            True if successful, False otherwise
        """
        print("🚀 MaSf-vision Bootstrap Tool")
        print("=" * 50)
        print(f"\nTarget repository: {self.target_repo}")
        print(f"Framework location: {self.framework_root}\n")
        
        try:
            # Step 1: Check prerequisites
            if not self._check_prerequisites():
                return False
            
            # Step 2: Set up directory structure
            if options.get('setup_dirs', True):
                print("\n📁 Step 1: Setting up directory structure...")
                self._setup_directories()
            
            # Step 3: Copy framework tools
            if options.get('copy_tools', True):
                print("\n🔧 Step 2: Copying framework tools...")
                self._copy_tools()
            
            # Step 4: Set up workflows
            if options.get('setup_workflows', True):
                print("\n⚙️  Step 3: Setting up GitHub workflows...")
                self._setup_workflows()
            
            # Step 5: Generate constitution from vision
            if options.get('generate_constitution', True):
                print("\n📜 Step 4: Generating PR constitution from vision...")
                self._generate_constitution()
            
            # Step 6: Create initial documentation
            if options.get('create_docs', True):
                print("\n📚 Step 5: Creating documentation...")
                self._create_docs()
            
            print("\n✅ Bootstrap complete!")
            print("\n📦 Next steps:")
            print("   1. Review your vision document in docs/product/vision.md")
            print("   2. Review the generated PR constitution in .github/agents/pr-merge-constitution.yaml")
            print("   3. Customize the workflows in .github/workflows/ if needed")
            print("   4. Commit and push the changes")
            print("   5. Open a PR to test the validation workflow")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Error during bootstrap: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _check_prerequisites(self) -> bool:
        """Check if prerequisites are met."""
        print("🔍 Checking prerequisites...")
        
        # Check if it's a git repository
        if not (self.target_repo / '.git').exists():
            print("⚠️  Warning: Not a git repository. Some features may not work.")
        else:
            print("✓ Git repository detected")
        
        # Check for vision document
        vision_locations = [
            self.target_repo / 'docs' / 'product' / 'vision.md',
            self.target_repo / 'docs' / 'vision.md',
            self.target_repo / 'VISION.md'
        ]
        
        vision_found = any(loc.exists() for loc in vision_locations)
        if not vision_found:
            print("⚠️  No vision document found. You'll need to create one.")
            print("   Expected locations:")
            for loc in vision_locations:
                print(f"   - {loc.relative_to(self.target_repo)}")
        else:
            print("✓ Vision document found")
        
        return True
    
    def _setup_directories(self):
        """Set up necessary directory structure."""
        dirs = [
            '.github/agents',
            '.github/workflows',
            'tools/agent-orchestration',
            'docs/product',
            'docs/adr'
        ]
        
        for dir_path in dirs:
            full_path = self.target_repo / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created {dir_path}")
    
    def _copy_tools(self):
        """Copy framework tools to target repository."""
        tools_to_copy = [
            'tools/agent-orchestration/pr-constitution-generator.py',
            'tools/agent-orchestration/master-agent.py',
            'tools/agent-orchestration/README-pr-constitution.md'
        ]
        
        for tool_path in tools_to_copy:
            src = self.framework_root / tool_path
            dst = self.target_repo / tool_path
            
            if src.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print(f"  ✓ Copied {tool_path}")
            else:
                print(f"  ⚠️  Tool not found: {tool_path}")
    
    def _setup_workflows(self):
        """Set up GitHub workflows."""
        workflows = [
            'pr-evaluation.yml'
        ]
        
        for workflow in workflows:
            src = self.framework_root / '.github' / 'workflows' / workflow
            dst = self.target_repo / '.github' / 'workflows' / workflow
            
            if src.exists():
                shutil.copy2(src, dst)
                print(f"  ✓ Copied workflow: {workflow}")
            else:
                print(f"  ⚠️  Workflow not found: {workflow}")
        
        # Copy agent templates
        agent_files = [
            'communication-protocol.md'
        ]
        
        for agent_file in agent_files:
            src = self.framework_root / '.github' / 'agents' / agent_file
            dst = self.target_repo / '.github' / 'agents' / agent_file
            
            if src.exists():
                shutil.copy2(src, dst)
                print(f"  ✓ Copied agent template: {agent_file}")
    
    def _generate_constitution(self):
        """Generate PR constitution from vision."""
        # Import and run the generator using importlib to handle hyphenated filename
        try:
            import importlib.util
            
            # Load the pr-constitution-generator.py module
            generator_path = self.target_repo / 'tools' / 'agent-orchestration' / 'pr-constitution-generator.py'
            spec = importlib.util.spec_from_file_location("pr_constitution_generator", generator_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            PRConstitutionGenerator = module.PRConstitutionGenerator
            
            generator = PRConstitutionGenerator(repo_root=str(self.target_repo))
            output_path = self.target_repo / '.github' / 'agents' / 'pr-merge-constitution.yaml'
            
            constitution = generator.generate(output_path=str(output_path))
            print(f"  ✓ Constitution generated")
            
        except FileNotFoundError as e:
            print(f"  ⚠️  Vision document not found: {e}")
            print("     You'll need to create a vision document and run the generator manually:")
            print("     python tools/agent-orchestration/pr-constitution-generator.py")
        except Exception as e:
            print(f"  ⚠️  Error generating constitution: {e}")
            print("     You can run the generator manually after fixing the issue:")
            print("     python tools/agent-orchestration/pr-constitution-generator.py")
    
    def _create_docs(self):
        """Create initial documentation."""
        # Create a sample vision if it doesn't exist
        vision_path = self.target_repo / 'docs' / 'product' / 'vision.md'
        
        if not vision_path.exists():
            sample_vision = """# Project Vision

## Mission Statement

[Describe what your project aims to achieve]

## The Problem

### Current State
- [Describe the problem you're solving]

### Pain Points
1. [Key pain point 1]
2. [Key pain point 2]

## The Solution

### Core Concept
[Describe your solution approach]

### Key Differentiators
1. [What makes your solution unique]

## Guiding Principles

1. **[Principle 1]**: [Description]
2. **[Principle 2]**: [Description]
3. **[Principle 3]**: [Description]
4. **[Principle 4]**: [Description]
5. **[Principle 5]**: [Description]

## Constraints

- [Technical constraint 1]
- [Resource constraint 2]
- [Business constraint 3]

## Success Criteria

- [Success metric 1]
- [Success metric 2]
- [Success metric 3]

## Vision for Success

### Short Term (6-12 months)
- [Goal 1]
- [Goal 2]

### Long Term (3-5 years)
- [Goal 1]
- [Goal 2]
"""
            
            vision_path.parent.mkdir(parents=True, exist_ok=True)
            with open(vision_path, 'w') as f:
                f.write(sample_vision)
            print(f"  ✓ Created sample vision document: {vision_path.relative_to(self.target_repo)}")
            print("     Please customize this with your project's actual vision!")
        else:
            print(f"  ✓ Vision document already exists")
        
        # Create README about the framework
        readme_path = self.target_repo / 'MASF-FRAMEWORK.md'
        if not readme_path.exists():
            readme_content = """# MaSf-vision Framework

This repository uses the MaSf-vision (Multi-Agent System Framework based on vision) framework.

## What is MaSf-vision?

MaSf-vision is a framework that enables autonomous AI agents to understand your project vision,
self-organize, and execute collaboratively to realize that vision.

## Key Components

### 1. Vision Document
Your project vision in `docs/product/vision.md` defines:
- Mission and purpose
- Core principles
- Goals and success criteria
- Constraints

### 2. PR Constitution
Generated from your vision, the PR constitution (`.github/agents/pr-merge-constitution.yaml`)
defines validation rules for pull requests that align with your principles.

### 3. Automated Workflows
GitHub Actions workflows automatically validate PRs against your constitution.

## Usage

### Updating Vision
When your vision evolves, update `docs/product/vision.md` and regenerate the constitution:

```bash
python tools/agent-orchestration/pr-constitution-generator.py
```

### PR Validation
Every PR is automatically checked against your constitution. The workflow will:
1. Validate core principles are followed
2. Check technical requirements
3. Verify code quality
4. Ensure security standards

## Documentation

- [PR Constitution Generator](tools/agent-orchestration/README-pr-constitution.md)
- [Vision Document](docs/product/vision.md)
- [PR Merge Constitution](.github/agents/pr-merge-constitution.yaml)

## Learn More

Visit the [MaSf-vision repository](https://github.com/McFuzzySquirrel/MaSf-vision) for more information.
"""
            with open(readme_path, 'w') as f:
                f.write(readme_content)
            print(f"  ✓ Created framework README: {readme_path.relative_to(self.target_repo)}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Bootstrap MaSf-vision framework into your repository',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Bootstrap into current directory
  python bootstrap.py

  # Bootstrap into specific directory
  python bootstrap.py --target-repo /path/to/repo

  # Bootstrap without creating sample docs
  python bootstrap.py --no-create-docs
        """
    )
    
    parser.add_argument(
        '--target-repo',
        help='Target repository path (default: current directory)',
        default=None
    )
    
    parser.add_argument(
        '--no-setup-dirs',
        action='store_true',
        help='Skip directory setup'
    )
    
    parser.add_argument(
        '--no-copy-tools',
        action='store_true',
        help='Skip copying framework tools'
    )
    
    parser.add_argument(
        '--no-setup-workflows',
        action='store_true',
        help='Skip workflow setup'
    )
    
    parser.add_argument(
        '--no-generate-constitution',
        action='store_true',
        help='Skip constitution generation'
    )
    
    parser.add_argument(
        '--no-create-docs',
        action='store_true',
        help='Skip documentation creation'
    )
    
    args = parser.parse_args()
    
    options = {
        'setup_dirs': not args.no_setup_dirs,
        'copy_tools': not args.no_copy_tools,
        'setup_workflows': not args.no_setup_workflows,
        'generate_constitution': not args.no_generate_constitution,
        'create_docs': not args.no_create_docs
    }
    
    bootstrap = MaSfBootstrap(target_repo=args.target_repo)
    success = bootstrap.bootstrap(options)
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
