import os
import pandas as pd
import numpy as np

# ==========================================
# Google Colab Users:
# You can copy and paste this entire script into a Colab cell and run it.
# It will generate 'air_quality.csv' directly in your Colab files tab!
# ==========================================

# Set random seed for reproducibility
np.random.seed(42)

# Generate 1000 samples
num_samples = 1000

# Features
# Temperature between 10C and 40C
temperature = np.random.uniform(10, 40, num_samples)
# Humidity between 20% and 90%
humidity = np.random.uniform(20, 90, num_samples)
# PM2.5 between 0 and 200 (ug/m3)
pm25 = np.random.uniform(0, 200, num_samples)

# Target: AQI
# We create a linear relationship: AQI = 2.5 * PM2.5 + 0.1 * Humidity + 0.5 * Temperature + noise
noise = np.random.normal(0, 10, num_samples)
aqi = (2.5 * pm25) + (0.1 * humidity) + (0.5 * temperature) + noise

# Ensure AQI is not negative
aqi = np.maximum(aqi, 0)

# Create DataFrame
df = pd.DataFrame({
    'Temperature': temperature,
    'Humidity': humidity,
    'PM2.5': pm25,
    'AQI': aqi
})

# Save to CSV (resolving path reliably relative to script location)
output_dir = os.path.dirname(__file__) if '__file__' in globals() else '.'
output_file = os.path.join(output_dir, 'air_quality.csv')
df.to_csv(output_file, index=False)
print(f"Generated air_quality.csv with {num_samples} samples at: {output_file}")
