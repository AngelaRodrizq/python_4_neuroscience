#!/usr/bin/env python
"""
Example script demonstrating neural data simulation and PCA analysis.

This script can be run standalone to see the package in action.
"""

import numpy as np
import matplotlib.pyplot as plt
from python_4_neuroscience.neural_simulation import (
    generate_neural_population,
    generate_lfp_signal,
)
from python_4_neuroscience.pca_analysis import (
    prepare_data_for_pca,
    perform_pca,
    plot_variance_explained,
)


def main():
    """Run a complete neural data analysis pipeline."""
    print("Neural Data Analysis Example")
    print("=" * 50)

    # Generate neural population data
    print("\n1. Generating neural population activity...")
    n_neurons = 30
    duration = 5.0  # seconds
    population_activity = generate_neural_population(
        n_neurons=n_neurons, duration=duration, base_rate=15.0, seed=42
    )
    print(f"   Generated data: {n_neurons} neurons, {duration}s duration")
    print(f"   Total spikes: {np.sum(population_activity):.0f}")

    # Generate LFP signal
    print("\n2. Generating LFP signal...")
    time, lfp = generate_lfp_signal(
        duration=3.0, frequencies=(8.0, 30.0), amplitudes=(1.0, 0.5), seed=42
    )
    print(f"   Generated LFP: {len(lfp)} samples")
    print(f"   Time range: {time[0]:.2f}s to {time[-1]:.2f}s")

    # Perform PCA
    print("\n3. Performing PCA analysis...")
    prepared_data = prepare_data_for_pca(population_activity, normalize=True)
    pca, transformed_data = perform_pca(prepared_data, variance_threshold=0.90)
    print(f"   PCA components: {pca.n_components_}")
    print(f"   Variance explained: {np.sum(pca.explained_variance_ratio_):.2%}")

    # Create visualizations
    print("\n4. Creating visualizations...")
    fig = plot_variance_explained(pca)
    output_file = "/tmp/neural_analysis_results.png"
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    print(f"   Saved plot to: {output_file}")

    print("\n" + "=" * 50)
    print("Analysis complete! Check the output plot.")


if __name__ == "__main__":
    main()
