# Python Template for Neuroscience Data Analysis

This is a modern Python package template designed for neuroscience students and researchers to get started with neural data analysis and coding.

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

### Installation

```bash
# Clone the repository
git clone https://github.com/AngelaRodrizq/python_template.git
cd python_template

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

To adapt this template for your own project:

1. Replace `python_pkg_template` with your package name in:
   - `pyproject.toml`
   - `src/` directory name
   - Import statements
   - Documentation

2. Update metadata in `pyproject.toml`:
   - `name`
   - `description`
   - `authors`
   - `dependencies`

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

