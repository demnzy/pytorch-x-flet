# Day 2 - Module 6: PyTorch & Training the Model (80 mins)

Welcome to the core of the class. We are going to build a brain.

## 1. What is Machine Learning? (10 mins)

As discussed on Day 1, imagine a black box with three knobs on it (Knob 1, Knob 2, Knob 3). You put the Temperature, Humidity, and PM2.5 into the box, and a number pops out (the AQI). 

If the number is wrong, you slightly turn the knobs and try again. You keep turning the knobs millions of times until the box starts spitting out the correct AQI for any weather you feed it.

**That is Machine Learning.** 
- The "knobs" are called **Weights**.
- The "black box" is our **Model**.
- The process of turning the knobs until they are perfect is called **Training**.

## 2. Tensors: The Language of PyTorch (15 mins)

To do this math incredibly fast, PyTorch uses a special data structure called a **Tensor**.
A Tensor is simply a grid of numbers. If you have a normal Python List of numbers `[1, 2, 3]`, that can be converted into a 1D Tensor. A "list of lists" like `[[1, 2], [3, 4]]` is a 2D Tensor (like a spreadsheet grid). 

PyTorch relies on Tensors because computer graphics cards (GPUs) are specifically designed to do math on massive grids of numbers all at once.

## 3. The Dataset and DataLoader (15 mins)

When training, we can't just throw 10,000 rows of data at the model all at once; it would overwhelm the computer's memory.
- The `Dataset` (in our code, `AirQualityDataset`) organizes our Pandas data into PyTorch Tensors.
- The `DataLoader` acts like a **conveyor belt**. It groups our data into small "batches" (e.g., 32 rows at a time) and feeds them into the model one batch at a time.

## 4. The Neural Architecture (20 mins)

Let's look at the "blueprint" (Class) of our brain:

```python
import torch.nn as nn

# We use INHERITANCE here! Our model inherits from PyTorch's nn.Module
class AirQualityModel(nn.Module):
    def __init__(self):
        # We must call super().__init__() to let PyTorch set up the math engines
        super().__init__()
        
        # 3 inputs (Temp, Humidity, PM2.5) -> 1 output (AQI)
        self.linear = nn.Linear(3, 1) 

    def forward(self, x):
        return self.linear(x)
```
`nn.Linear(3, 1)` is our black box. It automatically creates 3 "knobs" (Weights) behind the scenes, one for each input, and connects them to 1 output. 

## 5. The Training Loop (15 mins)

How do we teach the model to turn the knobs correctly? We use a loop that repeats three steps over and over. Every full loop through all our data is called an **Epoch**.

1. **Guess (Forward Pass):** The model looks at the inputs and makes a blind guess at the AQI.
2. **Grade (Loss):** We use a Loss Function (like Mean Squared Error) to compare the model's guess to the actual correct AQI. If the guess is way off, the "Loss" is a huge number.
3. **Correct (Backward Pass / Optimizer):** This is the magic. PyTorch uses calculus (Gradient Descent) to figure out exactly which direction to turn the 3 knobs to make the Loss smaller next time. We use an **Optimizer** (like Stochastic Gradient Descent - SGD) to physically turn the knobs.

## 6. Exporting the Brain (5 mins)
Once the loop is done and the Loss is very low, our model is "Trained". We save the final, perfect positions of the knobs to a file called `model.pth`. We can now use this file anywhere!

---

# 🎯 Day 2 Checkpoint: The Brain Blueprint

It's time to build the blueprint for your AI!

**Your Task:**
1. In your Google Colab session, upload the `air_quality.csv` file to the left-hand files tab.
2. Write a short Python script using Pandas to read the CSV and `print(data.head())` to prove it loaded successfully.
3. Write the PyTorch `AirQualityModel` class exactly as shown in Section 4.
4. Instantiate the class: `model = AirQualityModel()`.
5. Pass a dummy Tensor through it: `print(model(torch.tensor([[25.0, 50.0, 20.0]])))`.
6. Look at the output. Does it make sense? (Hint: It shouldn't yet, because it hasn't been trained!)

*In Day 3, we will fully train this model and hook it up to a beautiful user interface!*
