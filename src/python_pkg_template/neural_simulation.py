"""
Neural data simulation module for educational purposes.

This module provides simple tools for simulating neural activity data
commonly encountered in neuroscience research.
"""

import numpy as np
from typing import Tuple, Optional


def generate_spike_train(
    rate: float,
    duration: float,
    dt: float = 0.001,
    refractory_period: float = 0.002,
    seed: Optional[int] = None,
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Generate a Poisson spike train.

    Args:
        rate: Firing rate in Hz
        duration: Duration of the spike train in seconds
        dt: Time step in seconds (default: 1ms)
        refractory_period: Refractory period in seconds (default: 2ms)
        seed: Random seed for reproducibility

    Returns:
        Binary array where 1 indicates a spike at that time step
    """
    if seed is not None:
        np.random.seed(seed)

    n_steps = int(duration / dt)
    spike_train = np.zeros(n_steps)
    refractory_steps = int(refractory_period / dt)

    # Generate spikes based on Poisson process
    prob_spike = rate * dt

    i = 0
    while i < n_steps:
        if np.random.random() < prob_spike:
            spike_train[i] = 1
            i += refractory_steps  # Skip refractory period
        else:
            i += 1

    return spike_train


def generate_neural_population(
    n_neurons: int,
    duration: float,
    base_rate: float = 10.0,
    rate_variance: float = 5.0,
    dt: float = 0.001,
    seed: Optional[int] = None,
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Generate activity from a population of neurons.

    Args:
        n_neurons: Number of neurons in the population
        duration: Duration of recording in seconds
        base_rate: Mean firing rate across the population in Hz
        rate_variance: Standard deviation of firing rates in Hz
        dt: Time step in seconds
        seed: Random seed for reproducibility

    Returns:
        2D array of shape (n_neurons, n_time_steps) with spike trains
    """
    if seed is not None:
        np.random.seed(seed)

    # Generate firing rates for each neuron
    rates = np.random.normal(base_rate, rate_variance, n_neurons)
    rates = np.maximum(rates, 0.1)  # Ensure positive rates

    # Generate spike trains for each neuron
    n_steps = int(duration / dt)
    population_activity = np.zeros((n_neurons, n_steps))

    for i in range(n_neurons):
        population_activity[i, :] = generate_spike_train(
            rate=rates[i], duration=duration, dt=dt, seed=seed + i if seed else None
        )

    return population_activity


def add_noise(
    signal: np.ndarray,  # type: ignore[type-arg]
    noise_level: float = 0.1,
    seed: Optional[int] = None,
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Add Gaussian noise to a signal.

    Args:
        signal: Input signal array
        noise_level: Standard deviation of noise relative to signal std
        seed: Random seed for reproducibility

    Returns:
        Noisy signal
    """
    if seed is not None:
        np.random.seed(seed)

    signal_std = np.std(signal)
    noise = np.random.normal(0, noise_level * signal_std, signal.shape)
    return signal + noise  # type: ignore[no-any-return]


def generate_lfp_signal(
    duration: float,
    sampling_rate: float = 1000.0,
    frequencies: Tuple[float, ...] = (4.0, 8.0, 30.0),
    amplitudes: Tuple[float, ...] = (1.0, 0.5, 0.3),
    noise_level: float = 0.1,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray]:  # type: ignore[type-arg]
    """
    Generate a simulated Local Field Potential (LFP) signal.

    Args:
        duration: Duration in seconds
        sampling_rate: Sampling rate in Hz
        frequencies: Tuple of frequency components in Hz
        amplitudes: Tuple of amplitudes for each frequency
        noise_level: Noise standard deviation
        seed: Random seed for reproducibility

    Returns:
        Tuple of (time_array, lfp_signal)
    """
    if seed is not None:
        np.random.seed(seed)

    if len(frequencies) != len(amplitudes):
        raise ValueError("frequencies and amplitudes must have the same length")

    n_samples = int(duration * sampling_rate)
    time = np.linspace(0, duration, n_samples)

    # Generate signal as sum of sinusoids
    signal = np.zeros(n_samples)
    for freq, amp in zip(frequencies, amplitudes):
        signal += amp * np.sin(2 * np.pi * freq * time)

    # Add noise
    signal = add_noise(signal, noise_level, seed)

    return time, signal  # type: ignore[return-value]


def bin_spike_train(
    spike_train: np.ndarray, bin_size: int, method: str = "sum"  # type: ignore[type-arg]
) -> np.ndarray:  # type: ignore[type-arg]
    """
    Bin a spike train into larger time windows.

    Args:
        spike_train: Binary spike train array
        bin_size: Number of time steps per bin
        method: Binning method ('sum' or 'mean')

    Returns:
        Binned spike train
    """
    n_bins = len(spike_train) // bin_size
    reshaped = spike_train[: n_bins * bin_size].reshape(n_bins, bin_size)

    if method == "sum":
        return np.sum(reshaped, axis=1)  # type: ignore[no-any-return]
    elif method == "mean":
        return np.mean(reshaped, axis=1)  # type: ignore[no-any-return]
    else:
        raise ValueError(f"Unknown method: {method}. Use 'sum' or 'mean'")
