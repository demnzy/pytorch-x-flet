import os
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from torch.utils.data import Dataset, DataLoader

# ==========================================
# Google Colab Users:
# Make sure you have run 'generate_data.py' first so that 'air_quality.csv' 
# exists in your Colab files tab. You can then copy and paste this entire 
# script into a cell to train your model!
# ==========================================
# Session 2: Deep Dive into PyTorch
# Goal: Build an Air Quality Prediction Model
# ==========================================

# 1. Define a Custom Dataset to load our CSV
class AirQualityDataset(Dataset):
    def __init__(self, csv_file):
        # Read the CSV file using pandas
        self.data = pd.read_csv(csv_file)
        
        # We separate the input features (Temperature, Humidity, PM2.5) 
        # from our target variable (AQI)
        self.features = self.data[['Temperature', 'Humidity', 'PM2.5']].values
        self.targets = self.data['AQI'].values
        
        # Convert them to PyTorch Tensors (the core data structure in PyTorch)
        # We use float32 as it's standard for neural networks
        self.features = torch.tensor(self.features, dtype=torch.float32)
        self.targets = torch.tensor(self.targets, dtype=torch.float32).view(-1, 1)

    def __len__(self):
        # Tells PyTorch how many samples we have
        return len(self.data)

    def __getitem__(self, idx):
        # Returns a single sample (features, target) based on index
        return self.features[idx], self.targets[idx]

# 2. Define the Linear Regression Model
# In PyTorch, we build models by creating a class that inherits from nn.Module
class AirQualityModel(nn.Module):
    def __init__(self):
        super(AirQualityModel, self).__init__()
        # nn.Linear is a fully connected layer (y = xA^T + b)
        # We have 3 input features (Temp, Humidity, PM2.5) and 1 output (AQI)
        self.linear = nn.Linear(3, 1)

    def forward(self, x):
        # This defines how the data flows through our model
        return self.linear(x)

def train():
    # 3. Setup Data Loading
    base_dir = os.path.dirname(__file__) if '__file__' in globals() else '.'
    csv_file = os.path.join(base_dir, 'air_quality.csv')
    model_save_path = os.path.join(base_dir, 'model.pth')

    print(f"Loading data from {csv_file}...")
    dataset = AirQualityDataset(csv_file)
    
    # DataLoader handles batching our data automatically
    # Batch size of 32 means we update our model after every 32 samples
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    
    # 4. Initialize Model, Loss Function, and Optimizer
    model = AirQualityModel()
    
    # Mean Squared Error (MSE) is standard for regression problems
    criterion = nn.MSELoss() 
    
    # Stochastic Gradient Descent (SGD) with a small learning rate (lr)
    # The learning rate controls how big of a step we take to adjust our weights
    # We use 1e-6 because if the learning rate is too high, the model won't converge (Loss goes to NaN!)
    # (Note: In practice, we usually normalize our data to avoid having to use such small learning rates)
    optimizer = optim.SGD(model.parameters(), lr=1e-6)
    
    epochs = 100
    print("Starting training...")
    
    # 5. The Training Loop
    for epoch in range(epochs):
        epoch_loss = 0.0
        
        for batch_features, batch_targets in dataloader:
            # Step 1: Forward pass (make predictions)
            predictions = model(batch_features)
            
            # Step 2: Compute the loss (how wrong were we?)
            loss = criterion(predictions, batch_targets)
            
            # Step 3: Backward pass (calculate gradients)
            # We zero the gradients first so they don't accumulate
            optimizer.zero_grad()
            loss.backward()
            
            # Step 4: Update weights using the optimizer
            optimizer.step()
            
            epoch_loss += loss.item()
            
        # Print progress every 10 epochs
        if (epoch + 1) % 10 == 0:
            avg_loss = epoch_loss / len(dataloader)
            print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}")

    # 6. Save the trained model
    print("Training complete! Saving model...")
    # We use state_dict() to save the learned weights and biases
    torch.save(model.state_dict(), model_save_path)
    print(f"Model saved to {model_save_path}")

if __name__ == "__main__":
    train()
