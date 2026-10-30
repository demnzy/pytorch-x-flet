# Day 1 - Module 4: The Python Ecosystem (20 mins)

Python is powerful because you don't have to write everything from scratch. Millions of developers have written code that you can download and use.

## 1. Imports (10 mins)

When you want to use code written by someone else (or even code in another file you wrote), you have to tell Python to bring it into your script. You do this using the `import` keyword.

### `import`
```python
import math
print(math.pi) # Prints 3.14159...
```

### `import ... as ...`
Sometimes the name of the package is too long to type repeatedly. You can give it a nickname.
```python
import pandas as pd # We bring in pandas, but call it 'pd' for short
```

### `from ... import ...`
If a package is massive, and you only want one specific tool from it, you can just import that one tool.
```python
from train_model import AirQualityModel
```
This tells Python: "Look in the `train_model.py` file, and only bring the `AirQualityModel` blueprint into this file."

## 2. Installing Packages (10 mins)

As mentioned in Module 0, if you are working locally, you use a tool called `pip` (Python's package installer) to download tools from the internet:
```powershell
pip install torch pandas flet
```
*Note: If you are using Google Colab, packages like PyTorch and Pandas are already installed for you!*

---

# 🎯 Day 1 Checkpoint: The Dummy Predictor

You've learned about Variables, Functions, and basic Math. It's time to build your first "Predictor". 

**Your Task:**
1. Open a Google Colab notebook (or a local Python file).
2. Create a function called `calculate_dummy_aqi(temp, humidity, pm25)`.
3. Inside the function, write a simple math formula to guess the AQI. For example: `aqi = (temp * 0.5) + (humidity * 0.1) + (pm25 * 2.5)`.
4. `return` the calculated AQI.
5. Outside the function, create 3 variables for today's weather.
6. Call your function and `print()` the result to the screen!

*Once you've completed this, you are ready for Day 2, where we will replace our manual math formula with a real Machine Learning AI!*
