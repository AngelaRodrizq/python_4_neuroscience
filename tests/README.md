# Tests

## Why Write Tests?

Tests help you:
- Make sure your code works correctly
- Catch bugs before they cause problems
- Safely make changes (tests will alert you if something breaks)
- Document how your code should be used

## How to Write a Test

1. **Create a test file:** Name it `test_<description>.py`
   - Example: `test_my_analysis.py`

2. **Write test functions:** Each function should test one specific thing
   ```python
   def test_my_function_with_valid_input():
       # Setup: Create some test data
       test_data = [1, 2, 3, 4, 5]
       
       # Action: Run your function
       result = my_function(test_data)
       
       # Assert: Check the result is correct
       assert result == expected_value
       assert isinstance(result, int)
   ```

3. **Run your tests:**
   ```bash
   pytest
   ```

## Test Naming Convention

- **File names:** `test_*.py` (e.g., `test_neural_simulation.py`)
- **Function names:** `test_*` (e.g., `test_generate_spike_train`)

Pytest will automatically find and run all files and functions that match these patterns!

## Example Test

```python
# test_my_analysis.py

from your_package_name.neural_simulation import generate_spike_train
import numpy as np

def test_generate_spike_train_creates_array():
    """Test that generate_spike_train returns a numpy array."""
    result = generate_spike_train(duration=1.0, rate=10.0, seed=42)
    assert isinstance(result, np.ndarray)

def test_generate_spike_train_respects_seed():
    """Test that using the same seed gives the same results."""
    result1 = generate_spike_train(duration=1.0, rate=10.0, seed=42)
    result2 = generate_spike_train(duration=1.0, rate=10.0, seed=42)
    np.testing.assert_array_equal(result1, result2)

def test_generate_spike_train_times_in_range():
    """Test that spike times are within the specified duration."""
    duration = 5.0
    result = generate_spike_train(duration=duration, rate=10.0, seed=42)
    assert all(0 <= t <= duration for t in result)
```

## Running Tests

```bash
# Run all tests
pytest

# Run with more details
pytest -v

# Run tests in a specific file
pytest tests/test_my_analysis.py

# Run a specific test function
pytest tests/test_my_analysis.py::test_generate_spike_train_creates_array

# Run with coverage report
pytest --cov=src/your_package_name
```

## Tips for Good Tests

1. **Test edge cases:** Empty inputs, very large numbers, negative values
2. **Test one thing at a time:** Each test should check one specific behavior
3. **Use descriptive names:** `test_function_returns_positive_numbers` is better than `test_1`
4. **Keep tests simple:** Tests should be easier to understand than the code they test
5. **Don't test external libraries:** Trust that numpy, scipy, etc. work correctly

## Learn More

- Official pytest docs: https://docs.pytest.org/
- Real Python tutorial: https://realpython.com/pytest-python-testing/
