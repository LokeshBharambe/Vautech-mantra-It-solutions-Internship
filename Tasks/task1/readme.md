## VAUTECH SOLUTIONS — AI INTERNSHIP REPORT  
## Task 1: Real-World Dataset Sourcing & Problem Framing  

---

## Project Title  
Customer Purchase Prediction using Machine Learning  

## Intern Details  

- **Intern Name:** Lokesh Girish Bharambe  
- **Intern ID:** VT26AI001  
- **Domain:** Artificial Intelligence & Data Science  
- **Mentor:** Vishal Ramkumar Rajbhar  
- **Company:** Vautech Solutions IT Solutions  

---

## Project Overview  

This project is part of Task-1 of the internship program: **Real-World Dataset Sourcing & Problem Framing**.  
The objective is to identify a real-world business problem, source a relevant dataset, and perform initial **Exploratory Data Analysis (EDA)** using Python and Pandas.

---

## Industry Use Case Domain  

**E-Commerce**

---

## Business Problem  

Understanding customer purchasing behavior helps businesses:  

- Improve marketing strategies  
- Personalize recommendations  
- Increase sales and customer retention  

---

## AI Problem Type  

**Data Exploration & Pattern Identification**  
(Foundation for future prediction and recommendation tasks)

---

## Dataset  

- **Dataset Name:** Customer Purchase Data  
- **Source:** Open Dataset (Kaggle / Public Repository)  
- **File Name:** `customer_purchase_data.csv`

---

## Dataset Description  

| Feature                 | Description             |
|-------------------------|-------------------------|
| Age                     | Customer's age          |
| Gender                  | Encoded gender          | 
| Annual Income           | Yearly Income           |
| Number Of Purchases     | Past purchases          |
| Product Category        | Product category        |
| Time Spent On Website   | Time spent (minutes)    |
| Loyalty Program         | Membership Status       |
| Discounted Availed      | Discounts used          |
| Purchases Status        | Target variable         |

---

## Objectives  

- Load and inspect the dataset  
- Understand data structure and attributes  
- Generate summary statistics  
- Identify missing values  
- Prepare data for further modeling tasks  

---

## Tools & Technologies  

- Python 3.x  
- Pandas Library  

### Install Pandas (if needed)

pip install pandas

## Code Implementation

import pandas as pd
df = pd.read_csv("customer_purchase_data.csv")
print(df.head())
print(df.info())
print(df.describe())

missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

## Exploratory Data Analysis Summary

- Checked dataset shape and column data types
- Identified missing values
- Observed purchase amount distributions
- Found relationships between income and spending behavior

## Key Insights

- Dataset contains 1500 customer records  
- No missing values in any column  
- Mix of numerical behavioral and demographic features  
- Dataset is clean and ready for preprocessing and modeling  

## future Scope
- Perform data preprocessing and feature engineering
- Build machine learning models for purchase prediction
- Develop customer recommendation systems
- Implement customer segmentation analysis
- Visualize insights using Matplotlib / Seaborn

## Output  

- Dataset Entries: 1500 rows  
- Total Columns: 9  
- Data Types: int64 (7 columns), float64 (2 columns)  
- Memory Usage: 105.6 KB  
- Missing Values: None (0 missing in all columns)  

### Columns Information

| Column Name            | Data Type | Non-Null Count |
|------------------------|-----------|----------------|
| Age                    | int64     | 1500 |
| Gender                | int64     | 1500 |
| AnnualIncome          | float64   | 1500 |
| NumberOfPurchases     | int64     | 1500 |
| ProductCategory       | int64     | 1500 |
| TimeSpentOnWebsite    | float64   | 1500 |
| LoyaltyProgram        | int64     | 1500 |
| DiscountsAvailable    | int64     | 1500 |
| PurchaseStatus        | int64     | 1500 |


## Conclusion

This task successfully demonstrates real-world dataset sourcing, business problem framing, and initial exploratory data analysis.
The dataset is now prepared for advanced analytics such as:
- Customer segmentation
- Purchase prediction
- Recommendation systems
