"""
Tests for the pca_analysis module.
"""

import numpy as np
import pytest
from python_pkg_template.pca_analysis import (
    prepare_data_for_pca,
    perform_pca,
    plot_variance_explained,
    plot_pca_projection,
    reconstruct_from_pca,
    get_component_loadings,
)


@pytest.fixture
def sample_neural_data():
    """Create sample neural data for testing."""
    np.random.seed(42)
    # 10 neurons, 100 time steps
    return np.random.randn(10, 100)


def test_prepare_data_for_pca(sample_neural_data):
    """Test data preparation for PCA."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)

    # Check shape is transposed
    assert prepared.shape == (100, 10)

    # Check normalization (should have zero mean and unit variance)
    means = np.mean(prepared, axis=0)
    stds = np.std(prepared, axis=0)

    np.testing.assert_array_almost_equal(means, np.zeros(10), decimal=10)
    np.testing.assert_array_almost_equal(stds, np.ones(10), decimal=10)


def test_prepare_data_for_pca_no_normalization(sample_neural_data):
    """Test data preparation without normalization."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=False)

    # Check shape is transposed
    assert prepared.shape == (100, 10)

    # Check data is just transposed, not normalized
    np.testing.assert_array_equal(prepared, sample_neural_data.T)


def test_perform_pca(sample_neural_data):
    """Test PCA computation."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, transformed = perform_pca(prepared, n_components=5)

    # Check transformed shape
    assert transformed.shape == (100, 5)

    # Check PCA model attributes
    assert len(pca.explained_variance_ratio_) == 5
    assert 0 < np.sum(pca.explained_variance_ratio_) <= 1


def test_perform_pca_variance_threshold(sample_neural_data):
    """Test PCA with variance threshold."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, transformed = perform_pca(prepared, variance_threshold=0.8)

    # Check that we preserve at least 80% variance
    cumulative_variance = np.sum(pca.explained_variance_ratio_)
    assert cumulative_variance >= 0.8


def test_plot_variance_explained(sample_neural_data):
    """Test variance explained plotting."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, _ = perform_pca(prepared, n_components=5)

    fig = plot_variance_explained(pca)

    # Check that a figure was created
    assert fig is not None

    # Check that it has 2 subplots
    assert len(fig.axes) == 2


def test_plot_pca_projection(sample_neural_data):
    """Test PCA projection plotting."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, transformed = perform_pca(prepared, n_components=3)

    # Test without labels
    fig = plot_pca_projection(transformed, pc_x=0, pc_y=1)
    assert fig is not None
    assert len(fig.axes) == 1

    # Test with labels
    labels = np.random.randint(0, 3, size=100)
    fig = plot_pca_projection(transformed, pc_x=0, pc_y=1, labels=labels)
    assert fig is not None


def test_reconstruct_from_pca(sample_neural_data):
    """Test reconstruction from PCA."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    # Use all components for perfect reconstruction
    pca, transformed = perform_pca(prepared, n_components=10)

    # Reconstruct using all components
    reconstruction = reconstruct_from_pca(pca, transformed)
    assert reconstruction.shape == prepared.shape

    # Reconstruction should be close to original with all components
    np.testing.assert_array_almost_equal(reconstruction, prepared, decimal=10)


def test_reconstruct_from_pca_partial(sample_neural_data):
    """Test partial reconstruction from PCA."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, transformed = perform_pca(prepared, n_components=5)

    # Reconstruct using only 2 components
    reconstruction = reconstruct_from_pca(pca, transformed, n_components=2)
    assert reconstruction.shape == prepared.shape

    # Partial reconstruction should differ from original
    assert not np.allclose(reconstruction, prepared)


def test_get_component_loadings(sample_neural_data):
    """Test getting component loadings."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, _ = perform_pca(prepared, n_components=5)

    loadings = get_component_loadings(pca)

    # Check shape: should be (n_features, n_components)
    assert loadings.shape == (10, 5)


def test_get_component_loadings_with_names(sample_neural_data):
    """Test getting component loadings with feature names."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, _ = perform_pca(prepared, n_components=5)

    feature_names = [f"neuron_{i}" for i in range(10)]
    loadings = get_component_loadings(pca, feature_names=feature_names)

    assert loadings.shape == (10, 5)


def test_get_component_loadings_wrong_names(sample_neural_data):
    """Test error handling with wrong number of feature names."""
    prepared = prepare_data_for_pca(sample_neural_data, normalize=True)
    pca, _ = perform_pca(prepared, n_components=5)

    feature_names = [f"neuron_{i}" for i in range(5)]  # Wrong number
    with pytest.raises(ValueError):
        get_component_loadings(pca, feature_names=feature_names)
