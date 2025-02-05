To automatically add `install_requires` in `setup.py`, you can use a `requirements.txt` file and parse it in `setup.py`. This ensures that your dependencies are consistent across both files. Here's how you can do it:

---

### **Step 1: Create a `requirements.txt` File**
List your dependencies in `requirements.txt`:
```txt
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
requests>=2.31.0
```

---

### **Step 2: Modify `setup.py` to Read `requirements.txt`**
Update your `setup.py` to read the dependencies from `requirements.txt`:
```python
from setuptools import setup, find_packages
from pathlib import Path

# Read requirements.txt
def get_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"
    with open(requirements_file, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements(),  # Automatically add dependencies
)
```

---

### **Step 3: Install the Project**
Run the following command to install the project in editable mode:
```bash
pip install -e .
```

---

### **How It Works**
1. **`get_requirements()` Function**:
   - Reads the `requirements.txt` file.
   - Filters out comments (lines starting with `#`) and empty lines.
   - Returns a list of dependencies.

2. **`install_requires`**:
   - Passes the list of dependencies to `setup()`.

---

### **Step 4: Keep `requirements.txt` and `setup.py` in Sync**
Whenever you update `requirements.txt`, the `install_requires` in `setup.py` will automatically reflect the changes.

---

### **Alternative: Use `pip-tools` for Advanced Dependency Management**
If your project has complex dependencies (e.g., dev vs. production), you can use `pip-tools` to manage them.

1. **Install `pip-tools`**:
   ```bash
   pip install pip-tools
   ```

2. **Create `requirements.in`**:
   Add your dependencies to `requirements.in`:
   ```txt
   pandas>=2.0.0
   numpy>=1.24.0
   matplotlib>=3.7.0
   requests>=2.31.0
   ```

3. **Compile `requirements.txt`**:
   ```bash
   pip-compile requirements.in --output-file requirements.txt
   ```

4. **Update `setup.py`**:
   Use the same `get_requirements()` function as above to read `requirements.txt`.

---

### **Benefits of This Approach**
- **Single Source of Truth**: Dependencies are defined in one place (`requirements.txt` or `requirements.in`).
- **Consistency**: Ensures `setup.py` and `requirements.txt` are always in sync.
- **Flexibility**: Works with both simple and complex dependency setups.

---

### **Full Example**
Here’s the complete `setup.py`:
```python
from setuptools import setup, find_packages
from pathlib import Path

def get_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"
    with open(requirements_file, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements(),
)
```

And the `requirements.txt`:
```txt
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
requests>=2.31.0
```

---

### **Step 5: Test the Setup**
1. Install the project:
   ```bash
   pip install -e .
   ```

2. Verify the dependencies:
   ```bash
   pip freeze
   ```

You should see the dependencies (`pandas`, `numpy`, etc.) installed in your environment.

---
- for adding new requirements
append them in `requirement.txt`

-- for first time installation 

run 
```shell
./pre_requisit.sh
```

- for creating wheel file and building .whl file
run 
```shell
./runner.sh
```