"""
Tests for the neural_simulation module.
"""

import numpy as np
import pytest
from python_pkg_template.neural_simulation import (
    generate_spike_train,
    generate_neural_population,
    add_noise,
    generate_lfp_signal,
    bin_spike_train,
)


def test_generate_spike_train():
    """Test spike train generation."""
    spike_train = generate_spike_train(rate=10.0, duration=1.0, seed=42)

    # Check output is binary
    assert np.all((spike_train == 0) | (spike_train == 1))

    # Check length
    assert len(spike_train) == 1000  # 1 second at 1ms resolution

    # Check reproducibility
    spike_train2 = generate_spike_train(rate=10.0, duration=1.0, seed=42)
    np.testing.assert_array_equal(spike_train, spike_train2)


def test_generate_spike_train_rate():
    """Test that spike train respects firing rate approximately."""
    rate = 50.0
    duration = 10.0
    dt = 0.001

    spike_train = generate_spike_train(rate=rate, duration=duration, dt=dt, seed=42)

    # Count spikes and calculate observed rate
    n_spikes = np.sum(spike_train)
    observed_rate = n_spikes / duration

    # Should be within 20% of expected rate (Poisson variability)
    assert 0.8 * rate < observed_rate < 1.2 * rate


def test_generate_neural_population():
    """Test neural population generation."""
    n_neurons = 10
    duration = 1.0

    population = generate_neural_population(
        n_neurons=n_neurons, duration=duration, seed=42
    )

    # Check shape
    assert population.shape == (n_neurons, 1000)

    # Check all values are binary
    assert np.all((population == 0) | (population == 1))

    # Check reproducibility
    population2 = generate_neural_population(
        n_neurons=n_neurons, duration=duration, seed=42
    )
    np.testing.assert_array_equal(population, population2)


def test_add_noise():
    """Test noise addition."""
    # Use a signal with variation so std is not zero
    signal = np.sin(np.linspace(0, 10, 100))
    noisy_signal = add_noise(signal, noise_level=0.1, seed=42)

    # Check length unchanged
    assert len(noisy_signal) == len(signal)

    # Check that noise was added (signal changed)
    assert not np.allclose(signal, noisy_signal)

    # Check reproducibility
    noisy_signal2 = add_noise(signal, noise_level=0.1, seed=42)
    np.testing.assert_array_equal(noisy_signal, noisy_signal2)


def test_generate_lfp_signal():
    """Test LFP signal generation."""
    duration = 1.0
    time, lfp = generate_lfp_signal(duration=duration, seed=42)

    # Check lengths match
    assert len(time) == len(lfp)

    # Check time array is correct
    assert time[0] == 0
    assert time[-1] == pytest.approx(duration, rel=0.01)

    # Check reproducibility
    time2, lfp2 = generate_lfp_signal(duration=duration, seed=42)
    np.testing.assert_array_equal(lfp, lfp2)


def test_generate_lfp_signal_frequencies():
    """Test LFP with mismatched frequencies and amplitudes."""
    with pytest.raises(ValueError):
        generate_lfp_signal(duration=1.0, frequencies=(4.0, 8.0), amplitudes=(1.0,))


def test_bin_spike_train_sum():
    """Test spike train binning with sum method."""
    spike_train = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])
    binned = bin_spike_train(spike_train, bin_size=2, method="sum")

    expected = np.array([1, 2, 0, 1, 1])
    np.testing.assert_array_equal(binned, expected)


def test_bin_spike_train_mean():
    """Test spike train binning with mean method."""
    spike_train = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])
    binned = bin_spike_train(spike_train, bin_size=2, method="mean")

    expected = np.array([0.5, 1.0, 0.0, 0.5, 0.5])
    np.testing.assert_array_equal(binned, expected)


def test_bin_spike_train_invalid_method():
    """Test binning with invalid method."""
    spike_train = np.array([1, 0, 1, 1])
    with pytest.raises(ValueError):
        bin_spike_train(spike_train, bin_size=2, method="invalid")
