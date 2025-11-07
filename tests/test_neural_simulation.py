"""
Tests for the neural_simulation module.
"""

import numpy as np
from python_4_neuroscience.neural_simulation import (
    generate_spike_train,
    generate_neural_population,
    generate_lfp_signal,
)


def test_generate_spike_train():
    """Test basic spike train generation."""
    spike_train = generate_spike_train(rate=10.0, duration=1.0, seed=42)
    assert np.all((spike_train == 0) | (spike_train == 1))
    assert len(spike_train) == 1000


def test_generate_neural_population():
    """Test neural population generation."""
    population = generate_neural_population(n_neurons=10, duration=1.0, seed=42)
    assert population.shape == (10, 1000)
    assert np.all((population == 0) | (population == 1))


def test_generate_lfp_signal():
    """Test LFP signal generation."""
    time, lfp = generate_lfp_signal(duration=1.0, seed=42)
    assert len(time) == len(lfp)
    assert time[0] == 0
