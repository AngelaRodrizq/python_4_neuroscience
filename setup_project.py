#!/usr/bin/env python3
"""
Setup script to help students customize the Python package template.

This script will guide you through renaming the package and updating
all necessary files to use your chosen package name.
"""

import os
import re
import sys
from pathlib import Path


def is_valid_package_name(name: str) -> bool:
    """Check if the package name is valid for Python."""
    # Package names should be lowercase with underscores
    pattern = r'^[a-z][a-z0-9_]*$'
    return bool(re.match(pattern, name))


def get_package_name() -> str:
    """Prompt user for a valid package name."""
    print("\n" + "="*70)
    print("Welcome to the Python Template Setup!")
    print("="*70)
    print("\nThis script will help you customize this template for your project.")
    print("\nPackage naming rules:")
    print("  - Must start with a lowercase letter")
    print("  - Can only contain lowercase letters, numbers, and underscores")
    print("  - Examples: my_package, neuroscience_analysis, spike_analyzer")
    print()
    
    while True:
        name = input("Enter your desired package name (or 'quit' to exit): ").strip()
        
        if name.lower() == 'quit':
            print("Setup cancelled.")
            sys.exit(0)
        
        if not name:
            print("❌ Package name cannot be empty. Please try again.\n")
            continue
            
        if not is_valid_package_name(name):
            print(f"❌ '{name}' is not a valid package name.")
            print("   Remember: lowercase letters, numbers, and underscores only.")
            print("   Must start with a letter.\n")
            continue
        
        if name == "python_pkg_template":
            print("⚠️  You're using the default name. Consider choosing a more specific name.\n")
            confirm = input("Continue with 'python_pkg_template'? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                return name
            continue
        
        # Confirm with user
        print(f"\n✓ Package name: {name}")
        confirm = input("Is this correct? (yes/no): ").strip().lower()
        if confirm in ['yes', 'y']:
            return name
        print()


def update_file_content(file_path: Path, old_name: str, new_name: str) -> bool:
    """Update package name in a file. Returns True if changes were made."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Replace various forms of the package name
        replacements = [
            (old_name, new_name),  # python_pkg_template -> new_name
            (old_name.replace('_', '-'), new_name.replace('_', '-')),  # python-pkg-template
        ]
        
        new_content = content
        for old, new in replacements:
            new_content = new_content.replace(old, new)
        
        if new_content != content:
            file_path.write_text(new_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"⚠️  Warning: Could not update {file_path}: {e}")
        return False


def rename_directory(old_path: Path, new_name: str) -> Path:
    """Rename a directory to use the new package name."""
    new_path = old_path.parent / new_name
    old_path.rename(new_path)
    return new_path


def main():
    """Main setup function."""
    # Ensure we're in the project root
    project_root = Path(__file__).parent.absolute()
    os.chdir(project_root)
    
    old_package_name = "python_pkg_template"
    src_dir = project_root / "src"
    old_package_dir = src_dir / old_package_name
    
    # Check if already customized
    if not old_package_dir.exists():
        print("\n⚠️  It looks like this template has already been customized!")
        print("The default 'python_pkg_template' directory was not found.")
        sys.exit(1)
    
    # Get new package name from user
    new_package_name = get_package_name()
    
    print(f"\n{'='*70}")
    print("Starting setup...")
    print(f"{'='*70}\n")
    
    # Files to update
    files_to_update = [
        project_root / "pyproject.toml",
        project_root / "README.md",
        project_root / "CONTRIBUTING.md",
        project_root / "setup.py",
    ]
    
    # Add all Python files in src/
    if old_package_dir.exists():
        files_to_update.extend(old_package_dir.rglob("*.py"))
    
    # Add all test files
    test_dir = project_root / "tests"
    if test_dir.exists():
        files_to_update.extend(test_dir.rglob("*.py"))
    
    # Add all notebook files
    notebooks_dir = project_root / "notebooks"
    if notebooks_dir.exists():
        files_to_update.extend(notebooks_dir.rglob("*.ipynb"))
    
    # Add documentation files
    docs_dir = project_root / "docs"
    if docs_dir.exists():
        files_to_update.extend(docs_dir.rglob("*.md"))
        files_to_update.extend(docs_dir.rglob("*.yml"))
    
    # Update file contents
    updated_files = []
    for file_path in files_to_update:
        if file_path.is_file():
            if update_file_content(file_path, old_package_name, new_package_name):
                updated_files.append(file_path)
                print(f"✓ Updated: {file_path.relative_to(project_root)}")
    
    # Rename the package directory
    if old_package_dir.exists():
        new_package_dir = rename_directory(old_package_dir, new_package_name)
        print(f"\n✓ Renamed directory: src/{old_package_name} -> src/{new_package_name}")
    
    print(f"\n{'='*70}")
    print("Setup Complete!")
    print(f"{'='*70}\n")
    print(f"✓ Updated {len(updated_files)} files")
    print(f"✓ Package renamed from '{old_package_name}' to '{new_package_name}'")
    print("\nNext steps:")
    print("  1. Review the changes (run: git status)")
    print("  2. Install the package: pip install -e \".[develop]\"")
    print("  3. Run tests to verify: pytest")
    print("  4. Start coding!\n")
    
    # Ask if user wants to install now
    install = input("Would you like to install the package now? (yes/no): ").strip().lower()
    if install in ['yes', 'y']:
        print("\nInstalling package...")
        os.system('pip install -e ".[develop]"')
        print("\n✓ Installation complete!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
