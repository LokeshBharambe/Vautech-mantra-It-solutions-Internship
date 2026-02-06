import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load dataset
data = pd.read_csv("C:\\Users\\lokes\\OneDrive\\Desktop\\Vautech Internship\\Task 2\\loan_prediction.csv")

# Count missing values represented by '?'
# print(data=='?'.sum())  
# Python reads this as: '?' .sum()
# But '?' is a string 
# strings don't have a .sum() method

# Correct way to count occurrences of '?' in the DataFrame
# print((data == '?').sum())

print("Initial Dataset Shape:", data.shape)
print(data.head())

# Replace '?' with NaN(empty,null) values 
data.replace("?", np.nan, inplace=True)

# Step 2: Handle Missing Values
num_cols = data.select_dtypes(include=np.number).columns
data[num_cols] = data[num_cols].fillna(data[num_cols].mean())

cat_cols = data.select_dtypes(include='object').columns
for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Step 3: Remove Duplicates
data = data.drop_duplicates()

# Step 4: Handle Inconsistent Data
for col in cat_cols:
    data[col] = data[col].str.lower().str.strip()

# Step 5: Outlier Removal using IQR
Q1 = data[num_cols].quantile(0.25)
Q3 = data[num_cols].quantile(0.75)
IQR = Q3 - Q1

data = data[~((data[num_cols] < (Q1 - 1.5 * IQR)) |
              (data[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Step 6: Feature Encoding
le = LabelEncoder()
for col in cat_cols:
    data[col] = le.fit_transform(data[col])

# Step 7: Feature Scaling
scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])

# Step 8: Save Clean Dataset
data.to_csv("loan_prediction_clean.csv", index=False)

print("Final Clean Dataset Shape:", data.shape)
print("Clean dataset saved as loan_prediction_clean.csv")
