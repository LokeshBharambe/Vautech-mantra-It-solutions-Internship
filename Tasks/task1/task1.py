import pandas as pd

df = pd.read_csv("C:\\Users\\lokes\\OneDrive\\Desktop\\Vautech Internship\\Task 1\\customer_purchase_data.csv")
df.head()
df.info()
df.describe()

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)
