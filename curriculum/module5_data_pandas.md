# Day 2 - Module 5: Data Science & Pandas (40 mins)

Welcome to Day 2! Today we will start building our Machine Learning Model. But before an AI can learn, it needs something to learn *from*. That "something" is Data.

## 1. Pandas: Excel on Steroids (25 mins)

When humans look at data, we like to use Microsoft Excel or Google Sheets. We like rows, columns, and headers.
When Python looks at data, it uses a package called **Pandas**. 

Pandas gives Python the ability to read `.csv` files (which are just simple text versions of Excel spreadsheets) and turn them into what Pandas calls a **DataFrame**. A DataFrame is just code-speak for "a spreadsheet table."

```python
import pandas as pd

# This reads our CSV file and turns it into a DataFrame
data = pd.read_csv('air_quality.csv')
```

### Slicing the DataFrame with Lists
Once we have our data, we need to separate the Features (inputs) from the Target (output) so we can teach our model. We do this by feeding a Python **List** of column names into the DataFrame.

```python
# We use double brackets because we are feeding a List into the data 
features = data[['Temperature', 'Humidity', 'PM2.5']]

# If it's just one column, a single bracket is fine
targets = data['AQI']
```

## 2. Deconstructing `generate_data.py` (15 mins)

In the real world, you would go to a website like Kaggle and download a CSV file containing thousands of real-world recordings of air quality.

For this class, we wrote a script called `generate_data.py` to magically create a fake, but mathematically realistic, dataset for us. It uses a tool called **NumPy** (Number Python) to generate random numbers.

Here is the secret formula our generator used behind the scenes to calculate the AQI based on the random weather it generated:
`AQI = (Temperature * 1.5) + (Humidity * 0.5) + (PM2.5 * 2.0) + Base Level`

**Why is this important?**
Because we are *not* going to tell our Machine Learning model this formula! Instead, we are going to give our model the Features (Temp, Humidity) and the Targets (the final AQI), and force the model to **figure out the formula by itself**.

That process of "figuring it out" is called training, which is exactly what we will do in Module 6!
