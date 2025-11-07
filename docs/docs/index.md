# Python Template for Neuroscience Data Analysis

Welcome to the documentation for the Python Neuroscience Template! This package provides tools for simulating and analyzing neural data, designed specifically for neuroscience students learning Python.

## Overview

This template includes:

- **Neural Simulation Module**: Generate realistic spike trains, population activity, and LFP signals
- **PCA Analysis Module**: Perform dimensionality reduction on neural data
- **Example Notebooks**: Interactive tutorials demonstrating complete analysis pipelines
- **Modern Python Setup**: 2025 best practices with latest tooling

## Quick Start

### Installation

```bash
pip install -e ".[develop,notebooks]"
```

### Basic Example

```python
from python_pkg_template.neural_simulation import generate_neural_population
from python_pkg_template.pca_analysis import prepare_data_for_pca, perform_pca

# Generate simulated neural data
population = generate_neural_population(
    n_neurons=50, 
    duration=5.0, 
    base_rate=15.0
)

# Perform PCA
data = prepare_data_for_pca(population, normalize=True)
pca, transformed = perform_pca(data, variance_threshold=0.90)

print(f"Variance explained: {sum(pca.explained_variance_ratio_):.2%}")
```

## Modules

### Neural Simulation

The `neural_simulation` module provides functions to generate:

- **Spike Trains**: Poisson process-based spike generation
- **Population Activity**: Multi-neuron recordings
- **LFP Signals**: Local field potentials with multiple frequency components
- **Data Processing**: Binning and noise addition utilities

### PCA Analysis

The `pca_analysis` module provides tools for:

- **Data Preparation**: Normalization and formatting
- **PCA Computation**: Automatic component selection
- **Visualization**: Variance plots and 2D/3D projections
- **Reconstruction**: Inverse transform from components

## Tutorials

Check out the [example notebook](../notebooks/neural_data_analysis_tutorial.ipynb) for a complete walkthrough of:

1. Generating neural spike trains
2. Simulating population activity
3. Creating LFP signals
4. Performing PCA analysis
5. Visualizing results

## Documentation

Find more information on [material-mkdocs here](https://squidfunk.github.io/mkdocs-material/).
