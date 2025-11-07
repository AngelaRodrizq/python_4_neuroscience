# Python Template for Neuroscience Data Analysis

This is a modern Python package template designed for neuroscience students and researchers to get started with neural data analysis and coding.

> **👋 Never programmed before?** Start with our [QUICKSTART.md](QUICKSTART.md) guide for absolute beginners!

## 🎓 For Students: First Time Setup

If you're new to Python or programming, follow these steps carefully:

### Prerequisites

Before you begin, make sure you have:
- **Python 3.10 or newer** installed ([Download here](https://www.python.org/downloads/))
  - To check: Open a terminal and type `python --version` or `python3 --version`
- **Git** installed ([Download here](https://git-scm.com/downloads))
  - To check: Type `git --version` in your terminal
- **A text editor** like VS Code ([Download here](https://code.visualstudio.com/))

### Step-by-Step Setup for Beginners

#### 1. Get a Copy of This Template

```bash
# Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux)

# Navigate to where you want to create your project
cd ~/Documents  # or wherever you keep your projects

# Download this template
git clone https://github.com/AngelaRodrizq/python_template.git

# Go into the project folder
cd python_template
```

#### 2. Customize Your Package Name

**This is important!** You should rename the package to match your project.

```bash
# Run the setup script - it will guide you through the process
python setup_project.py
```

The script will ask you to choose a package name. For example:
- If you're analyzing spike data: `spike_analyzer`
- If you're working with calcium imaging: `calcium_analysis`
- If you're doing general neural analysis: `my_neural_analysis`

**Rules for package names:**
- Use only lowercase letters
- Use underscores (`_`) instead of spaces
- Start with a letter, not a number
- Good: `spike_analyzer`, `neural_data_tools`
- Bad: `Spike-Analyzer`, `123data`, `my package`

#### 3. Install Your Package

After running the setup script, install your newly named package:

```bash
# Install in "editable" mode so you can modify the code
pip install -e ".[develop,notebooks]"
```

**What does this do?**
- `-e` means "editable" - changes you make to the code will take effect immediately
- `.[develop,notebooks]` installs your package plus development tools and Jupyter

This might take a few minutes as it downloads required libraries.

#### 4. Verify Everything Works

```bash
# Run the tests to make sure everything is set up correctly
pytest

# You should see output like "5 passed" - that means it worked!
```

#### 5. Start Exploring!

Try opening one of the example notebooks:

```bash
# Start Jupyter
jupyter notebook

# Then open: notebooks/neural_data_analysis_tutorial.ipynb
```

### 🆘 Common Issues for Beginners

**"python: command not found"**
- Try `python3` instead of `python`
- Make sure Python is installed and added to your PATH

**"pip: command not found"**
- Try `pip3` instead of `pip`
- Or use: `python -m pip` or `python3 -m pip`

**"Permission denied" errors**
- On Mac/Linux, don't use `sudo` with pip
- Consider using a virtual environment (see Advanced Setup below)

**Tests are failing**
- Make sure you ran `pip install -e ".[develop]"` first
- Try reinstalling: `pip install -e ".[develop]" --force-reinstall`

## Features

### 2025 Best Practices
* **Modern Python**: Requires Python 3.10+ with latest stable dependencies
* **PEP 518 Standard**: Uses `pyproject.toml` for project configuration
* **Advanced Tooling**: Includes `ruff` for fast linting alongside `black` formatting
* **Type Safety**: `mypy` support for type checking
* **Pre-commit Hooks**: Automated code quality checks
* **GitHub Actions**: CI/CD pipeline for testing and deployment
* **Documentation**: Static documentation site with mkdocs-material

### Neuroscience Modules
* **Neural Simulation**: Generate realistic spike trains, population activity, and LFP signals
* **PCA Analysis**: Perform dimensionality reduction and visualization of neural data
* **Example Notebooks**: Interactive tutorials demonstrating complete analysis pipelines

## Quick Start

> **New to Python?** See the [🎓 For Students: First Time Setup](#-for-students-first-time-setup) section above for detailed beginner instructions!

### Quick Installation (For Experienced Users)

```bash
# Clone the repository
git clone https://github.com/AngelaRodrizq/python_template.git
cd python_template

# Customize the package name (optional but recommended)
python setup_project.py

# Install the package in development mode
pip install -e ".[develop,notebooks]"
```

### Basic Usage

```python
from python_pkg_template.neural_simulation import generate_neural_population
from python_pkg_template.pca_analysis import prepare_data_for_pca, perform_pca

# Generate simulated neural data
population_activity = generate_neural_population(
    n_neurons=50,
    duration=5.0,
    base_rate=15.0,
    seed=42
)

# Perform PCA
prepared_data = prepare_data_for_pca(population_activity, normalize=True)
pca, transformed_data = perform_pca(prepared_data, variance_threshold=0.90)

print(f"Variance explained: {sum(pca.explained_variance_ratio_):.2%}")
```

### Interactive Tutorial

Explore the complete tutorial notebook:

```bash
jupyter notebook notebooks/neural_data_analysis_tutorial.ipynb
```

## Package Structure

```
python_template/
├── src/python_pkg_template/    # Main package code
│   ├── neural_simulation.py    # Neural data simulation tools
│   ├── pca_analysis.py         # PCA analysis tools
│   └── __init__.py
├── tests/                       # Test suite
│   ├── test_neural_simulation.py
│   ├── test_pca_analysis.py
│   └── simple_test.py
├── notebooks/                   # Jupyter notebooks
│   └── neural_data_analysis_tutorial.ipynb
├── docs/                        # Documentation
├── scripts/                     # Standalone scripts
├── pyproject.toml              # Project configuration
└── README.md
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/python_pkg_template
```

### Code Quality

```bash
# Format code
black src/ tests/

# Run linter
ruff check src/ tests/

# Type checking
mypy src/ tests/
```

### Pre-commit Hooks

Install pre-commit hooks to automatically format and check code:

```bash
pre-commit install
```

## Dependencies

### Core Dependencies
* `numpy >= 1.26.0` - Numerical computing
* `scipy >= 1.11.0` - Scientific computing
* `matplotlib >= 3.8.0` - Plotting and visualization
* `scikit-learn >= 1.3.0` - Machine learning and PCA

### Development Dependencies
* `pytest` - Testing framework
* `black` - Code formatting
* `ruff` - Fast linting
* `mypy` - Type checking
* `pre-commit` - Git hooks

## Learning Resources

### For Neuroscience Students

This template is designed to help you:
1. **Learn Python Best Practices**: Modern project structure and tooling
2. **Understand Neural Data**: Simulate and analyze realistic neural activity
3. **Apply Dimensionality Reduction**: Use PCA to find patterns in high-dimensional data
4. **Build Analysis Pipelines**: Combine multiple tools into complete workflows

### Key Concepts Covered
* Spike trains and Poisson processes
* Neural population activity
* Local Field Potentials (LFP)
* Principal Component Analysis (PCA)
* Data normalization and preprocessing
* Visualization techniques

## Customization

### Easy Method: Use the Setup Script (Recommended for Beginners)

The easiest way to customize this template is to use the included setup script:

```bash
python setup_project.py
```

This interactive script will:
- Guide you through choosing a package name
- Automatically update all files with your new package name
- Rename directories appropriately
- Offer to install the package for you

### Manual Method: For Advanced Users

If you prefer to customize manually:

1. Replace `python_pkg_template` with your package name in:
   - `pyproject.toml` (the `name` and `[tool.setuptools.package-data]` fields)
   - Rename `src/python_pkg_template/` directory to `src/your_package_name/`
   - Update import statements in all Python files
   - Update references in documentation and notebooks

2. Update metadata in `pyproject.toml`:
   - `name`
   - `description`
   - `authors`
   - `dependencies` (if needed)

3. Customize the modules to your specific needs

## Documentation

Build and view the documentation locally:

```bash
pip install -e ".[build_docs]"
cd docs
mkdocs serve
```

Then visit http://localhost:8000

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

See LICENSE.txt for details.

## Citation

If you use this template in your research, please cite:

```bibtex
@software{python_neuroscience_template,
  title = {Python Template for Neuroscience Data Analysis},
  year = {2025},
  url = {https://github.com/AngelaRodrizq/python_template}
}
```

