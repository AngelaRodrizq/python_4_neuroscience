# Quick Start Guide for Absolute Beginners

Welcome! This guide will help you get started with this Python template, even if you've never programmed before.

## What You'll Learn

This template will help you:
- Write professional Python code
- Analyze neuroscience data (like neural spike trains)
- Learn modern programming practices
- Build your own data analysis tools

## Step 1: Install What You Need

### Install Python

1. Go to https://www.python.org/downloads/
2. Download Python 3.10 or newer
3. Run the installer
   - ⚠️ **Important on Windows:** Check the box that says "Add Python to PATH"
4. Test it worked:
   - Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux)
   - Type: `python --version`
   - You should see something like "Python 3.12.3"

### Install Git

1. Go to https://git-scm.com/downloads
2. Download and install Git for your operating system
3. Test it worked:
   - In your terminal, type: `git --version`
   - You should see something like "git version 2.40.0"

### Install a Code Editor (Optional but Recommended)

We recommend VS Code:
1. Go to https://code.visualstudio.com/
2. Download and install it
3. Open VS Code and install the Python extension

## Step 2: Get This Template

1. **Open your terminal**

2. **Navigate to where you want to keep your projects:**
   ```bash
   # On Mac/Linux:
   cd ~/Documents
   
   # On Windows:
   cd %USERPROFILE%\Documents
   ```

3. **Download the template:**
   ```bash
   git clone https://github.com/AngelaRodrizq/python_template.git
   ```

4. **Go into the project folder:**
   ```bash
   cd python_template
   ```

## Step 3: Customize Your Project

Run the setup script - it will help you rename the package:

```bash
python setup_project.py
```

**What to enter:**
- When asked for a package name, choose something that describes your project
- Use lowercase letters and underscores
- Examples: `my_neural_data`, `spike_analysis`, `brain_signals`

## Step 4: Install Your Package

After running the setup script, install your package:

```bash
# This will install your package and all tools you need
pip install -e ".[develop,notebooks]"
```

**This might take a few minutes.** It's downloading libraries for:
- Number crunching (numpy)
- Scientific computing (scipy)
- Making graphs (matplotlib)
- Machine learning (scikit-learn)
- Testing your code (pytest)

## Step 5: Test Everything Works

```bash
pytest
```

You should see output ending with "5 passed". If you do, congratulations! Everything is set up correctly! 🎉

## Step 6: Start Learning!

### Try the Tutorial Notebook

```bash
jupyter notebook
```

This will open a web browser. Click on:
- `notebooks/`
- `neural_data_analysis_tutorial.ipynb`

### Try Running Your Code

Create a new file called `my_first_script.py`:

```python
# Import from your package (use YOUR package name, not python_pkg_template)
from your_package_name.neural_simulation import generate_spike_train

# Generate some fake spike data
spike_times = generate_spike_train(duration=5.0, rate=10.0, seed=42)

# Print the results
print(f"Generated {len(spike_times)} spikes")
print(f"First 5 spike times: {spike_times[:5]}")
```

Run it:
```bash
python my_first_script.py
```

## Common Problems

### "python: command not found"

Try `python3` instead:
```bash
python3 setup_project.py
python3 -m pip install -e ".[develop,notebooks]"
```

### "pip: command not found"

Try:
```bash
python -m pip install -e ".[develop,notebooks]"
```

### "Permission denied"

**Don't use `sudo`!** Instead, you might need to:
1. Make sure Python is installed for your user
2. Or use a virtual environment (see Advanced Tips below)

### Tests are failing

1. Make sure you ran the installation command
2. Make sure you ran the setup script first
3. Try reinstalling:
   ```bash
   pip install -e ".[develop,notebooks]" --force-reinstall
   ```

## Advanced Tips

### Using a Virtual Environment

A virtual environment keeps your project's dependencies separate. This is a good practice:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Now install your package
pip install -e ".[develop,notebooks]"
```

When you're done working:
```bash
deactivate
```

### Learning More

- **Python basics**: Try https://www.learnpython.org/
- **Numpy tutorial**: https://numpy.org/doc/stable/user/quickstart.html
- **Jupyter notebooks**: https://jupyter-notebook-beginner-guide.readthedocs.io/

## Getting Help

If you're stuck:
1. Read the error message carefully - it often tells you what's wrong
2. Copy the error message and search for it online
3. Check the main [README.md](README.md) for more details
4. Ask in the GitHub issues

Remember: Everyone was a beginner once! Don't be afraid to ask questions. 🌟
