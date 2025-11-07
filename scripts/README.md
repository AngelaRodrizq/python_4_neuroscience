# Scripts for Your Project

If you write some scripts which are meant to be run stand-alone (not imported as part of the library), put them in this directory.

## What Goes Here?

**Standalone scripts** are Python files that you run directly, like:
- Data analysis scripts
- One-time data processing tasks
- Plotting scripts
- Scripts to download or prepare data

## What Doesn't Go Here?

**Reusable code** should go in the `src/` directory instead:
- Functions you import in multiple places
- Classes you use across your project
- Core analysis tools

## Example

```python
# This goes in scripts/
# scripts/analyze_my_data.py
from your_package_name.neural_simulation import generate_neural_population
from your_package_name.pca_analysis import perform_pca

# Load your data
data = load_my_experimental_data()

# Analyze it
results = perform_pca(data)

# Save results
save_results(results, "output.csv")
```

Run it with:
```bash
python scripts/analyze_my_data.py
```
