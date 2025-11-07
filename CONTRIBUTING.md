# Contributing

Thank you for your interest in contributing to this neuroscience data analysis template!

## 🎓 For Students: Your First Contribution

If this is your first time contributing to a code project, don't worry! Here's a simple guide:

### Understanding the Project

This template helps you:

- Write clean, well-organized Python code
- Analyze neuroscience data (like spike trains and neural activity)
- Learn professional coding practices

Before making changes, make sure you understand:

- What the code currently does
- How your change will improve it
- How to test that your change works

### Making Your First Change

1. **Make sure everything is set up:**

   ```bash
   # If you haven't already, run the setup script
   python setup_project.py
   
   # Install all development tools
   pip install -e ".[develop,notebooks]"
   ```

2. **Create a new branch for your changes:**

Run the following code or, alternatively, use the VS Code interface to create a branch of your own. The idea is that for any changes you want to make to the repository, you create a branch. Once everything is working, you create a pull request in the Github website.

   ```bash
   # Give your branch a descriptive name
   git checkout -b add-new-feature
   ```

3. **Make your changes:**
   - Edit the relevant Python files
   - Keep changes small and focused
   - Add comments if your code does something complex

4. **Test your changes:**

   ```bash
   # Run all tests
   pytest
   
   # Make sure your code looks good
   black src/ tests/
   ```

5. **Commit your changes:**

   ```bash
   # Stage your changes
   git add .
   
   # Commit with a clear message
   git commit -m "Add feature to analyze spike patterns"
   ```

## Getting Started

### Installation for Development

**For beginners:** If you haven't customized the template yet, follow these steps:

**Step 1: Clone the repository (if you haven't already)**

```bash
git clone https://github.com/AngelaRodrizq/python_4_neuroscience.git
cd python_4_neuroscience
```

**Step 2: Create a conda environment (recommended)**

```bash
# Create a new conda environment with Python 3.13
conda create --name neuroscience python=3.13

# Activate the environment
conda activate neuroscience
```

**Alternative: Using Python's built-in virtual environment**

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

**Step 3: Customize the package name (optional)**

```bash
# This helps you rename the package to match your project
python setup_project.py
```

**Step 4: Install all development tools**

```bash
# Install the package in development mode with all dependencies
pip install -e ".[develop,notebooks]"

# Install pre-commit hooks for automatic code formatting
pre-commit install
```

**What does this do?**

- `pip install -e ".[develop,notebooks]"` installs your package plus all tools needed for development
- `pre-commit install` sets up automatic code checking whenever you commit changes

## Development Workflow

### 1. Code Quality

We use several tools to maintain code quality:

- **Black**: Automatically formats your code to look consistent
- **Ruff**: Checks for common errors and style issues (linting)
- **MyPy**: Checks that you're using the right types of data
- **Pytest**: Runs tests to make sure your code works

**For beginners:** Run these commands before committing your changes:

```bash
# Format your code (fixes spacing, line length, etc. automatically)
black src/ tests/

# Check for issues (this will list any problems to fix)
ruff check src/ tests/

# Check types (makes sure you're not mixing up different kinds of data)
mypy src/ tests/

# Run tests (makes sure your changes didn't break anything)
pytest
```

**Tip:** The pre-commit hooks will run Black and Ruff automatically when you commit, so you might not need to run them manually!

### 2. Testing

All new features should include tests. **Why?** Tests help ensure:

- Your code works correctly
- Future changes don't break your feature
- Others can trust your code

**For beginners - How to write a test:**

```python
# In tests/test_my_feature.py

def test_my_new_function():
    """Test that my_new_function works correctly."""
    # 1. Prepare some test data
    test_input = [1, 2, 3, 4, 5]
    
    # 2. Run your function
    result = my_new_function(test_input)
    
    # 3. Check the result is what you expect
    assert result == 15  # Should sum to 15
    assert isinstance(result, int)  # Should be an integer
```

**Running tests:**

```bash
# Run all tests
pytest

# Run tests with more details (shows each test name)
pytest -v

# Run tests with coverage (shows which lines of code were tested)
pytest --cov=src/python_pkg_template

# Run only one test file
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
python_4_neuroscience/
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

- **Type Hints**: Help catch errors early and make code more understandable

  ```python
  def process_data(spike_times: list[float]) -> np.ndarray:
      # The type hints (list[float] and np.ndarray) tell you what goes in and out
  ```

- **Docstrings**: Document what functions do so others (and future you!) can understand them

  ```python
  def analyze_spikes(data):
      """
      Analyze spike train data.
      
      Args:
          data: Neural spike timing data
          
      Returns:
          Analysis results including firing rates
      """
  ```

- **Tests**: Ensure code works as expected and doesn't break when you make changes

  ```python
  def test_my_function():
      result = my_function(test_input)
      assert result == expected_output
  ```

- **Modularity**: Break code into small, reusable functions instead of one giant script

- **Version Control**: Use git to track changes, try new ideas safely, and collaborate

**Remember:** Everyone starts as a beginner! Don't hesitate to:

- Ask questions in issues
- Look at existing code for examples
- Start with small changes
- Learn by doing

## Questions?

If you have questions about contributing, please:

1. Check existing issues and discussions
2. Review the README and documentation
3. Open a new issue with your question
