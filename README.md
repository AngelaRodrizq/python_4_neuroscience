# Python Template for Neuroscience Data Analysis

## 🎓 For Students: First Time Setup

If you're new to Python or programming, follow these steps carefully:

### Prerequisites

Before you begin, make sure you have:

- **Conda** (Anaconda or Miniconda) installed ([Download here](https://docs.conda.io/en/latest/miniconda.html))
  - To check: Open a terminal and type `conda --version`
  - Alternatively, you can use Python 3.10 or newer directly ([Download here](https://www.python.org/downloads/))
- **Git** installed ([Download here](https://git-scm.com/downloads))
  - To check: Type `git --version` in your terminal
- **A text editor** like VS Code ([Download here](https://code.visualstudio.com/))

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/AngelaRodrizq/python_4_neuroscience.git
cd python_4_neuroscience

# Create and activate a conda environment (recommended)
conda create --name neuroscience python=3.13
conda activate neuroscience
```

Now, its time to change the package name for your own project.
The following script will ask you to choose a package name. For example:

- If you're analyzing spike data: `spike_analyzer`
- If you're working with calcium imaging: `calcium_analysis`
- If you're doing general neural analysis: `my_neural_analysis`

**Rules for package names:**

- Use only lowercase letters
- Use underscores (`_`) instead of spaces
- Start with a letter, not a number
- Good: `spike_analyzer`, `neural_data_tools`
- Bad: `Spike-Analyzer`, `123data`, `my package`

```bash
# Customize the package name (optional but recommended)
python setup_project.py
```

Finish your installation:

```bash
# Install the package in development mode
pip install -e ".[develop,notebooks]"

### Pre-commit Hooks
### Install pre-commit hooks to automatically format and check code:
pre-commit install
```

### Basic Usage

```python
from python_4_neuroscience.neural_simulation import generate_neural_population
from python_4_neuroscience.pca_analysis import prepare_data_for_pca, perform_pca

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
python_4_neuroscience/
├── src/python_4_neuroscience/    # Main package code
│   ├── ...                     # Here you will add new subfolders and files
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

## Dependencies

If you need to modify your packages and dependencies, edit the .toml file to the specific packages and versions you might need. If you check that file out, you'll see that the core dependencies that are already in it are the following:

### Core Dependencies

- `numpy >= 1.26.0` - Numerical computing

- `scipy >= 1.11.0` - Scientific computing
- `matplotlib >= 3.8.0` - Plotting and visualization
- `scikit-learn >= 1.3.0` - Machine learning and PCA

### Development Dependencies

- `pytest` - Testing framework

- `black` - Code formatting
- `ruff` - Fast linting
- `mypy` - Type checking
- `pre-commit` - Git hooks

## Learning Resources

### For Neuroscience Students

This template is designed to help you:

1. **Learn Python Best Practices**: Modern project structure and tooling
2. **Understand Neural Data**: Simulate and analyze realistic neural activity
3. **Apply Dimensionality Reduction**: Use PCA to find patterns in high-dimensional data
4. **Build Analysis Pipelines**: Combine multiple tools into complete workflows

### Manual Customization

If you prefer to customize manually, instead of using the setup file provided:

1. Replace `python_4_neuroscience` with your package name in:
   - `pyproject.toml` (the `name` and `[tool.setuptools.package-data]` fields)
   - Rename `src/python_4_neuroscience/` directory to `src/your_package_name/`
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

Then visit <http://localhost:8000>

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
  url = {https://github.com/AngelaRodrizq/python_4_neuroscience}
}
```
