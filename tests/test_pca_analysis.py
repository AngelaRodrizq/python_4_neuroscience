"""
Tests for the pca_analysis module.
"""

import numpy as np
from python_4_neuroscience.pca_analysis import (
    prepare_data_for_pca,
    perform_pca,
)


def test_prepare_data_for_pca():
    """Test data preparation for PCA."""
    np.random.seed(42)
    neural_data = np.random.randn(10, 100)
    prepared = prepare_data_for_pca(neural_data, normalize=True)
    assert prepared.shape == (100, 10)


def test_perform_pca():
    """Test PCA computation."""
    np.random.seed(42)
    neural_data = np.random.randn(10, 100)
    prepared = prepare_data_for_pca(neural_data, normalize=True)
    pca, transformed = perform_pca(prepared, n_components=5)
    assert transformed.shape == (100, 5)
    assert len(pca.explained_variance_ratio_) == 5
