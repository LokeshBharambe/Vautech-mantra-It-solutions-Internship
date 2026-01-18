# Customer Purchase Data Analysis

## 📌 Project Overview
This project performs basic exploratory data analysis (EDA) on a customer purchase dataset using Python and Pandas. The goal is to load the dataset, inspect its structure, generate summary statistics, and check for missing values.

---

## 📂 Dataset
The dataset file used in this project: 
        customer_purchase_data.csv
Make sure the file is placed in the correct directory before running the script.

---

## 🛠️ Requirements

- Python 3.x
- Pandas

Install Pandas if not already installed:
```bash
pip install pandas

---

💻 Code Explanation

import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\lokes\\OneDrive\\Desktop\\Vautech Internship\\Task 1\\customer_purchase_data.csv")

# Display first few rows
df.head()

# Display dataset information
df.info()

# Display statistical summary
df.describe()

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)