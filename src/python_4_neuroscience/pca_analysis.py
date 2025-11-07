"""
PCA analysis module for neural data.

This module provides tools for performing Principal Component Analysis (PCA)
on neural data, a fundamental dimensionality reduction technique in neuroscience.
"""

import numpy as np
from sklearn.decomposition import PCA
from typing import Tuple, Optional
import matplotlib.pyplot as plt


def prepare_data_for_pca(
    neural_data: np.ndarray, normalize: bool = True  # type: ignore[type-arg]
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Prepare neural data for PCA analysis.

    Args:
        neural_data: 2D array of shape (n_neurons, n_time_steps)
        normalize: Whether to normalize each neuron's activity

    Returns:
        Prepared data of shape (n_time_steps, n_neurons)
    """
    # Transpose to get samples x features format
    data = neural_data.T

    if normalize:
        # Normalize each neuron (feature) to have zero mean and unit variance
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        # Avoid division by zero
        std[std == 0] = 1
        data = (data - mean) / std

    return data  # type: ignore[no-any-return]


def perform_pca(
    data: np.ndarray,  # type: ignore[type-arg]
    n_components: Optional[int] = None,
    variance_threshold: float = 0.95,
) -> Tuple[PCA, np.ndarray]:  # type: ignore[type-arg]
    """
    Perform PCA on neural data.

    Args:
        data: Data array of shape (n_samples, n_features)
        n_components: Number of components to keep (if None, determined by variance_threshold)
        variance_threshold: Fraction of variance to preserve (default: 0.95)

    Returns:
        Tuple of (fitted PCA model, transformed data)
    """
    if n_components is None:
        # First fit with all components to determine n_components
        pca_temp = PCA()
        pca_temp.fit(data)
        cumulative_variance = np.cumsum(pca_temp.explained_variance_ratio_)
        n_components = int(np.argmax(cumulative_variance >= variance_threshold) + 1)

    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    return pca, transformed_data


def plot_variance_explained(
    pca: PCA, figsize: Tuple[int, int] = (12, 4), save_path: Optional[str] = None
) -> plt.Figure:
    """
    Plot the variance explained by principal components.

    Args:
        pca: Fitted PCA model
        figsize: Figure size (width, height)
        save_path: Path to save the figure (optional)

    Returns:
        Matplotlib figure object
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

    # Individual variance explained
    ax1.bar(
        range(1, len(pca.explained_variance_ratio_) + 1),
        pca.explained_variance_ratio_,
    )
    ax1.set_xlabel("Principal Component")
    ax1.set_ylabel("Variance Explained Ratio")
    ax1.set_title("Variance Explained by Each PC")
    ax1.grid(True, alpha=0.3)

    # Cumulative variance explained
    cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
    ax2.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker="o")
    ax2.axhline(y=0.95, color="r", linestyle="--", label="95% threshold")
    ax2.set_xlabel("Number of Components")
    ax2.set_ylabel("Cumulative Variance Explained")
    ax2.set_title("Cumulative Variance Explained")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig


def plot_pca_projection(
    transformed_data: np.ndarray,  # type: ignore[type-arg]
    pc_x: int = 0,
    pc_y: int = 1,
    labels: Optional[np.ndarray] = None,  # type: ignore[type-arg]
    figsize: Tuple[int, int] = (8, 6),
    save_path: Optional[str] = None,
) -> plt.Figure:
    """
    Plot data projected onto two principal components.

    Args:
        transformed_data: PCA-transformed data
        pc_x: Index of PC for x-axis (0-indexed)
        pc_y: Index of PC for y-axis (0-indexed)
        labels: Optional labels for coloring points
        figsize: Figure size (width, height)
        save_path: Path to save the figure (optional)

    Returns:
        Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=figsize)

    if labels is not None:
        scatter = ax.scatter(
            transformed_data[:, pc_x],
            transformed_data[:, pc_y],
            c=labels,
            cmap="viridis",
            alpha=0.6,
        )
        plt.colorbar(scatter, ax=ax, label="Label")
    else:
        ax.scatter(
            transformed_data[:, pc_x], transformed_data[:, pc_y], alpha=0.6, s=20
        )

    ax.set_xlabel(f"PC{pc_x + 1}")
    ax.set_ylabel(f"PC{pc_y + 1}")
    ax.set_title(f"Neural Data Projection: PC{pc_x + 1} vs PC{pc_y + 1}")
    ax.grid(True, alpha=0.3)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    return fig


def reconstruct_from_pca(
    pca: PCA,
    transformed_data: np.ndarray,  # type: ignore[type-arg]
    n_components: Optional[int] = None,
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Reconstruct original data from PCA components.

    Args:
        pca: Fitted PCA model
        transformed_data: PCA-transformed data
        n_components: Number of components to use for reconstruction
                     (if None, uses all available)

    Returns:
        Reconstructed data in original space
    """
    if n_components is not None and n_components < transformed_data.shape[1]:  # type: ignore[index]
        # Use only first n_components
        partial_data = transformed_data[:, :n_components]
        # Reconstruct
        reconstruction = pca.mean_ + np.dot(
            partial_data, pca.components_[:n_components]
        )
    else:
        reconstruction = pca.inverse_transform(transformed_data)

    return reconstruction  # type: ignore[no-any-return]


def get_component_loadings(
    pca: PCA, feature_names: Optional[list] = None
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Get the loadings (weights) of each feature on the principal components.

    Args:
        pca: Fitted PCA model
        feature_names: Optional list of feature names

    Returns:
        Array of component loadings (n_features, n_components)
    """
    loadings = pca.components_.T

    if feature_names is not None:
        if len(feature_names) != loadings.shape[0]:
            raise ValueError(
                f"Number of feature names ({len(feature_names)}) "
                f"must match number of features ({loadings.shape[0]})"
            )

    return loadings  # type: ignore[no-any-return]
