# 🧠 PyTorch & Flet Fundamentals: Machine Learning Bootcamp

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Flet](https://img.shields.io/badge/Flet-UI-007ACC.svg?logo=flutter&logoColor=white)](https://flet.dev/)
[![Colab Ready](https://img.shields.io/badge/Colab-Ready-F9AB00.svg?logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A structured, beginner-friendly **Machine Learning & Python Fundamentals training curriculum**. This repository contains a complete 3-day intensive bootcamp designed to take learners from zero programming or ML experience through data wrangling, tensor mathematics, and neural network training in PyTorch — culminating in a **bonus capstone desktop application** built with [Flet](https://flet.dev/).

---

## 📌 Repository Overview

This repository is organized primarily as an **educational training resource**. The core curriculum guides students step-by-step through the foundations of data science and deep learning:

1. **Python & OOP Primitives**: Variables, collections, functions, and class inheritance.
2. **Data Science with Pandas**: Synthetic dataset creation, feature engineering, and matrix operations.
3. **Machine Learning with PyTorch**: Tensors, custom `Dataset` and `DataLoader` pipelines, gradient descent, loss functions, and the training loop.
4. **Bonus Capstone Build (Flet UI)**: An interactive, glassmorphic desktop application that loads the trained PyTorch weights (`model.pth`) and executes real-time inference as the user adjusts live environment sliders.

> [!NOTE]
> **The Flet GUI was built as a bonus capstone deployment.** The primary mission of this repository is mastering Machine Learning and PyTorch fundamentals. The Flet app illustrates how a trained model can be taken out of a notebook and embedded into an interactive consumer application.

---

## ☁️ Google Colab & Hardware Accessibility

No powerful GPU or local setup is required for the machine learning modules:
* **Days 1 & 2 (Modules 0–6)**: Can be run entirely inside your browser using **Google Colab** with free cloud compute.
* **Day 3 (Modules 7–8 & Bonus App)**: Run locally on your machine to render the native desktop GUI window.

---

## 🗺️ Curriculum Schedule

Each day is structured for **2.5 hours (150 minutes)** of focused learning:

```
┌────────────────────────────────────────────────────────────────────────────┐
│ DAY 1: Setup, ML Foundations & Python Basics (150 mins)                   │
├────────────────────────────────────────────────────────────────────────────┤
│ • Module 0: Software Setup & Core ML Terminology                           │
│ • Module 1: Core Python Basics (Variables, Types, Conditionals)            │
│ • Module 2: Lists, Dictionaries & Reusable Functions                       │
│ • Module 3: Object-Oriented Programming (Classes & Inheritance)            │
│ • Module 4: The Python Ecosystem & Package Management                      │
│ 🎯 Checkpoint Project: The Dummy AQI Predictor                             │
└────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ DAY 2: Data Wrangling, PyTorch & Flet Intro (150 mins)                     │
├────────────────────────────────────────────────────────────────────────────┤
│ • Module 5: Data Science & Wrangling with Pandas                           │
│ • Module 6: PyTorch Deep Dive (Tensors, DataLoaders, Loss, Optimizer)      │
│ • Module 7 (Part 1): Introduction to Flet Controls & Layouts               │
│ 🎯 Checkpoint Project: The Brain Blueprint (AirQualityModel Architecture)  │
└────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ DAY 3: UI Polish & End-to-End Model Integration (150 mins)                │
├────────────────────────────────────────────────────────────────────────────┤
│ • Module 7 (Part 2): Modern Aesthetics, Glassmorphism & Event Handlers     │
│ • Module 8: The Grand Integration (Loading .pth weights into Flet)        │
│ 🎯 Checkpoint Project: Bonus Desktop App with Real-Time PyTorch Inference  │
└────────────────────────────────────────────────────────────────────────────┘
```

Detailed guides for all modules are located in the [`curriculum/`](curriculum/) directory:
* [`curriculum/day_by_day_schedule.md`](curriculum/day_by_day_schedule.md) — Complete timeline and breakdown.
* [`curriculum/module0_software_setup.md`](curriculum/module0_software_setup.md) — Environment setup & ML vocabulary.
* [`curriculum/module1_core_python.md`](curriculum/module1_core_python.md) — Python basics.
* [`curriculum/module2_lists_functions.md`](curriculum/module2_lists_functions.md) — Data structures and modular code.
* [`curriculum/module3_oop.md`](curriculum/module3_oop.md) — Classes, methods, and inheritance.
* [`curriculum/module4_ecosystem.md`](curriculum/module4_ecosystem.md) — Virtual environments, pip, and libraries.
* [`curriculum/module5_data_pandas.md`](curriculum/module5_data_pandas.md) — DataFrames and exploratory analysis.
* [`curriculum/module6_pytorch_ml.md`](curriculum/module6_pytorch_ml.md) — Neural network training with PyTorch.
* [`curriculum/module7_flet_ui.md`](curriculum/module7_flet_ui.md) — Modern GUI development with Flet.
* [`curriculum/module8_integration.md`](curriculum/module8_integration.md) — Connecting PyTorch models to user interfaces.

---

## 🏗️ Architecture & Data Pipeline

```
  [ generate_data.py ]
          │
          ▼ (Generates 1,000 synthetic sensor readings)
   air_quality.csv
   ├── Temperature (°C)
   ├── Humidity (%)
   ├── PM2.5 (µg/m³)
   └── AQI (Target)
          │
          ▼
  [ train_model.py ]
   ├── AirQualityDataset (PyTorch Dataset)
   ├── DataLoader (Batch size: 32, Shuffle: True)
   ├── AirQualityModel (nn.Linear(3, 1))
   ├── Loss: MSELoss() | Optimizer: SGD(lr=1e-6)
   └── Saves learned weights
          │
          ▼
      model.pth (Trained Weights)
          │
          ▼
  [ app.py (Bonus Build) ]
   ├── Loads model.pth with model.eval()
   ├── Glassmorphic UI Card (Blur, Border, Gradients)
   ├── Interactive Sliders (Temp, Humidity, PM2.5)
   └── Real-time AQI Prediction via torch.no_grad()
```

---

## ⚡ Quickstart & Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/demnzy/pytorch-x-flet.git
cd pytorch-x-flet
```

### 2. Set Up a Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate on Linux / macOS
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Workflow

### Step 1: Generate Dataset
Creates `air_quality.csv` containing 1,000 synthetic samples modeling physical relationships between temperature, humidity, particulate matter (PM2.5), and AQI:
```bash
python generate_data.py
```

### Step 2: Train the PyTorch Model
Trains a linear neural network (`AirQualityModel`) using mini-batch SGD and saves the weight checkpoint to `model.pth`:
```bash
python train_model.py
```
*Expected output:*
```
Loading data from air_quality.csv...
Starting training...
Epoch 10/100, Loss: 202.2853
Epoch 50/100, Loss: 103.0435
Epoch 100/100, Loss: 102.3705
Training complete! Saving model...
Model saved to model.pth
```

### Step 3: Run the Bonus Flet Application
Launch the real-time inference desktop monitor:
```bash
python app.py
```

Drag the sliders (Temperature, Humidity, PM2.5) to watch the PyTorch neural network predict the Air Quality Index (AQI) instantly with dynamic color coding (Green / Yellow / Orange / Red).

---

## 📁 Repository Structure

```
pytorch-x-flet/
├── curriculum/                          # 3-Day Intensive Training Curriculum
│   ├── day_by_day_schedule.md           # Master curriculum schedule & timeline
│   ├── module0_software_setup.md        # Environment setup & ML concepts
│   ├── module1_core_python.md           # Core Python basics
│   ├── module2_lists_functions.md       # Lists, dicts, and functions
│   ├── module3_oop.md                   # Object-oriented programming in Python
│   ├── module4_ecosystem.md             # Virtual environments & package managers
│   ├── module5_data_pandas.md           # Data processing with Pandas
│   ├── module6_pytorch_ml.md            # PyTorch models, tensors & training
│   ├── module7_flet_ui.md               # Flet UI foundations & glassmorphism
│   └── module8_integration.md           # End-to-end ML integration
├── air_quality.csv                      # Generated dataset for training
├── app.py                               # [Bonus Build] Glassmorphic Flet Desktop App
├── generate_data.py                     # Synthetic dataset generation script
├── model.pth                            # Trained PyTorch model weights checkpoint
├── train_model.py                       # PyTorch Dataset, Model & Training loop
├── requirements.txt                     # Python dependencies
├── .gitignore                           # Git ignore rules for caches & venv
└── README.md                            # Repository documentation
```

---

## 💡 Key Concepts Covered

### Machine Learning & PyTorch
* **`torch.Tensor`**: Creating, reshaping, and casting multidimensional numerical arrays.
* **`torch.utils.data.Dataset` & `DataLoader`**: Standardized data ingestion, indexing, and batch shuffling.
* **`torch.nn.Module`**: Defining layer graphs and the forward pass computation.
* **Loss Functions & Optimization**: Mean Squared Error (`nn.MSELoss`) and Stochastic Gradient Descent (`optim.SGD`).
* **Inference Best Practices**: Disabling autograd with `torch.no_grad()` and toggling evaluation mode with `model.eval()`.

### Flet & UI Engineering (Bonus Build)
* **Declarative Layouts**: Hierarchical structuring with `ft.Column`, `ft.Row`, and responsive containers.
* **Glassmorphic Styling**: Frosted glass effects via background opacity and blur filters (`ft.Blur`).
* **Event-Driven State**: Binding slider input events (`on_change`) to live ML inference routines.

---

## 📄 License

This training repository is open source and available under the [MIT License](LICENSE).
