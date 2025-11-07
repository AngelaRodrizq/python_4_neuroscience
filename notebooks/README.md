# Jupyter Notebooks

## What Are Jupyter Notebooks?

Jupyter notebooks are interactive documents that combine:
- **Code** that you can run and modify
- **Text** explaining what the code does
- **Graphs and visualizations** of your results
- **Equations** (if needed)

They're perfect for:
- Exploring data interactively
- Creating tutorials
- Sharing your analysis with others
- Prototyping before writing formal code

## Getting Started with Notebooks

### 1. Install Jupyter

If you haven't already:
```bash
pip install -e ".[notebooks]"
```

### 2. Start Jupyter

```bash
jupyter notebook
```

This will open a web browser showing your project files.

### 3. Try the Tutorial

Click on `neural_data_analysis_tutorial.ipynb` to see an example!

## Creating Your Own Notebook

1. **In the Jupyter web interface, click "New" → "Python 3"**

2. **You'll get an empty notebook with a cell. Try this:**
   ```python
   from your_package_name.neural_simulation import generate_spike_train
   import matplotlib.pyplot as plt
   
   # Generate some spikes
   spikes = generate_spike_train(duration=10.0, rate=5.0, seed=42)
   
   # Plot them
   plt.eventplot(spikes)
   plt.xlabel('Time (s)')
   plt.title('Spike Train')
   plt.show()
   ```

3. **Press Shift+Enter to run the cell**

## Notebook Tips for Beginners

### Basic Keyboard Shortcuts

- **Shift + Enter**: Run the current cell and move to the next one
- **Ctrl/Cmd + Enter**: Run the current cell and stay on it
- **Esc**: Exit edit mode
- **Enter**: Enter edit mode
- **A**: Add a cell above (when in command mode)
- **B**: Add a cell below (when in command mode)
- **DD**: Delete the current cell (press D twice)

### Best Practices

1. **Add markdown cells with explanations**
   - Press **Esc** then **M** to convert a cell to markdown
   - Write notes explaining what your code does

2. **Run cells in order**
   - Notebooks can get confusing if you run cells out of order
   - Use "Kernel → Restart & Run All" to test your notebook from scratch

3. **Save often**
   - Notebooks auto-save, but it's good to manually save important work
   - Use **Ctrl/Cmd + S**

4. **Name your notebooks descriptively**
   - Good: `calcium_imaging_analysis_2024-01-15.ipynb`
   - Bad: `Untitled1.ipynb`

## What to Put in This Directory

Store notebooks for:
- **Analysis workflows**: Step-by-step data analysis
- **Tutorials**: Teaching how to use your package
- **Exploration**: Trying out ideas interactively
- **Visualization**: Creating figures for papers/presentations

## Moving From Notebooks to Code

When your notebook code becomes reusable, move it to `src/`:

**Notebook (exploration):**
```python
# Trying out a new analysis in a notebook
def my_new_analysis(data):
    # ... code ...
    return results
```

**Package (reusable code):**
```python
# Move to src/your_package_name/analysis.py
def my_new_analysis(data):
    """
    Perform my new analysis.
    
    Args:
        data: Input data
        
    Returns:
        Analysis results
    """
    # ... same code ...
    return results
```

Then in your notebook, you can just:
```python
from your_package_name.analysis import my_new_analysis
```

## Learn More

- [Jupyter Documentation](https://jupyter.org/documentation)
- [Jupyter Notebook Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- [Gallery of Interesting Notebooks](https://github.com/jupyter/jupyter/wiki)
