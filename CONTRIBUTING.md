# Contributing

Thank you for your interest in contributing to this neuroscience data analysis template!

## Getting Started

### Installation for Development

```bash
# Clone the repository
git clone https://github.com/AngelaRodrizq/python_template.git
cd python_template

# Install the package in development mode with all dependencies
pip install -e ".[develop,notebooks]"

# Install pre-commit hooks for automatic code formatting
pre-commit install
```

## Development Workflow

### 1. Code Quality

We use several tools to maintain code quality:

- **Black**: Automatic code formatting
- **Ruff**: Fast Python linting
- **MyPy**: Static type checking
- **Pytest**: Testing framework

Run all checks before committing:

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/ tests/

# Run tests
pytest
```

### 2. Testing

All new features should include tests:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src/python_pkg_template

# Run specific test file
pytest tests/test_neural_simulation.py -v
```

### 3. Pre-commit Hooks

The pre-commit hooks will automatically:
- Format code with Black
- Lint with Ruff
- Check for common issues
- Strip notebook outputs

These run automatically when you commit, or manually with:

```bash
pre-commit run --all-files
```

### 4. Adding New Features

When adding new features:

1. Create tests first (test-driven development)
2. Implement the feature
3. Document the code with docstrings
4. Add examples to notebooks if relevant
5. Update README and docs

## Project Structure

```
python_template/
├── src/python_pkg_template/    # Main package code
│   ├── neural_simulation.py    # Neural data simulation
│   ├── pca_analysis.py         # PCA analysis tools
│   └── __init__.py
├── tests/                       # Test suite
├── notebooks/                   # Example notebooks
├── docs/                        # Documentation
└── scripts/                     # Standalone scripts
```

## For Students

This template is designed to teach best practices in scientific Python:

- **Type Hints**: Help catch errors early
- **Docstrings**: Document what functions do
- **Tests**: Ensure code works as expected
- **Modularity**: Break code into reusable functions
- **Version Control**: Use git effectively

Don't hesitate to ask questions or suggest improvements!

## Run CI Locally

To run the CI pipeline locally:

Setup (make sure docker is installed):
```bash
brew install act  # macOS
# or use appropriate package manager for your OS
```

Run the workflow:
```bash
act -j develop
```

## Questions?

If you have questions about contributing, please:
1. Check existing issues and discussions
2. Review the README and documentation
3. Open a new issue with your question
