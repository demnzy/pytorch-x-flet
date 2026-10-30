# Day 3 - Module 8: The Grand Integration (90 mins)

You have built a PyTorch Machine Learning model (`model.pth`), and you have built a beautiful user interface with Flet. Now, it is time to connect the brain to the body.

## 1. Waking up the Brain (30 mins)

In `app.py`, before we draw any UI elements, we need to load our PyTorch model from the file.

```python
import torch
import os
# We only want the AirQualityModel blueprint from train_model.py
from train_model import AirQualityModel 

# 1. Create the empty blueprint
model = AirQualityModel()

# 2. Find the saved brain file using __file__
model_path = os.path.join(os.path.dirname(__file__), 'model.pth')

# 3. Load the memories (the knobs/weights) into the blueprint
model.load_state_dict(torch.load(model_path, weights_only=True))

# 4. Put the brain in "Test Mode"
model.eval() 
```

**What is `__file__`?**
`__file__` is a hidden variable in Python that knows the exact folder where your script lives. By using `os.path.join(os.path.dirname(__file__), 'model.pth')`, we guarantee Python will always find the model file, no matter where you launch the app from.

## 2. Context Managers (`with`) and Predictions (60 mins)

When a user drags a slider in Flet, the value is just a normal Python number (e.g., `25.5`). But remember, PyTorch only speaks the language of **Tensors**.

When the user moves the slider, our `update_prediction` event handler springs into action:

```python
def predict_aqi(temperature, humidity, pm25):
    # Step 1: Translate to a Tensor using a list inside a list!
    input_tensor = torch.tensor([[temperature, humidity, pm25]], dtype=torch.float32)
    
    # Step 2: Ask the model using a Context Manager
    with torch.no_grad():
        prediction = model(input_tensor)
        
    # Step 3: Turn the Tensor back into a normal Python number
    return prediction.item() 
```
**Why the `with` statement?**
The `with` keyword creates a **Context Manager**. It's like walking into a sterile hospital room. 
`with torch.no_grad():` tells PyTorch: *"For everything indented below this line, completely turn off your learning engine to save memory. We are only predicting right now."* As soon as the indentation ends, PyTorch returns to normal.

---

# 🎯 Day 3 Checkpoint: The Final Integration

You made it! It is time to complete the app.

**Your Task:**
1. If you trained your model in Google Colab, download the `model.pth` file to your computer.
2. Open VS Code and ensure `model.pth`, `train_model.py`, and `app.py` are all in the same folder.
3. Finish writing your `app.py` using the beautiful Glassmorphic Flet code provided by your instructor.
4. Run `python app.py` in your terminal.
5. Drag the sliders. You should instantly see your trained Machine Learning model predicting the Air Quality in real-time!

**Congratulations!** You have generated data, built a Neural Network in PyTorch, constructed a modern UI in Flet, and integrated them into a fully functioning application. Welcome to the world of AI Engineering!
