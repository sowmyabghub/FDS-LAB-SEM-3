
# Experiment No: 11
# Experiment to Understand Pandas Library Use Cases in Data Science
# Description: Understand DataFrame use cases using Pandas library

import numpy as np
import pandas as pd

# Create a list of employee details
list1 = [[1, 'Smith', 50000],
         [2, 'Jones', 60000]]

# Create a DataFrame
df = pd.DataFrame(list1)
print("Original DataFrame:")
print(df)

# Assign column names
df.columns = ['Empd', 'Name', 'Salary']
print("\nDataFrame with Column Names:")
print(df)

# Display DataFrame information
print("\nDataFrame Information:")
df.info()

# Create a sample 50 Startups dataset
startup_data = {
    'R&D Spend': [165349.20, 162597.70, 153441.51, 144372.41, 142107.34],
    'Administration': [136897.80, 151377.59, 101145.55, 118671.85, 91391.77],
    'Marketing Spend': [471784.10, 443898.53, 407934.54, 383199.62, 366168.42],
    'State': ['New York', 'California', 'Florida', 'New York', 'Florida'],
    'Profit': [192261.83, 191792.06, 191050.39, 182901.99, 166187.94]
}

startup_df = pd.DataFrame(startup_data)
print("\nStartup DataFrame:")
print(startup_df)

print("\nFirst Five Rows of Startup Data:")
print(startup_df.head())

print("\nLast Five Rows of Startup Data:")
print(startup_df.tail())

print("\nStartup DataFrame Information:")
startup_df.info()

# Create employee dataset
employee_data = [
    [1, 'SREE VARSSINI K S', 5000],
    [2, 'SREEMATHI B', 6000],
    [3, 'SREYA G', 7000],
    [4, 'SREYASKARI MULLAPUDI', 5000],
    [5, 'SRI AKASH U G', 8000],
    [6, 'SRI HARSHAVARDHANAN R', 3000],
    [7, 'SRI HARSHAVARDHANAN R', 6000]
]

df = pd.DataFrame(employee_data, columns=['emp id', 'name', 'salary'])

print("\nEmployee DataFrame:")
print(df)

# Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Display last five rows
print("\nLast Five Rows:")
print(df.tail())

# Display information
print("\nEmployee DataFrame Information:")
df.info()

# Display salary column
print("\nSalary Column:")
print(df.salary)

# Display data type of salary column
print("\nType of Salary Column:")
print(type(df.salary))

# Calculate mean
print("\nMean Salary:")
print(df.salary.mean())

# Calculate median
print("\nMedian Salary:")
print(df.salary.median())

# Calculate mode
print("\nMode Salary:")
print(df.salary.mode())

# Calculate variance
print("\nSalary Variance:")
print(df.salary.var())

# Calculate standard deviation
print("\nSalary Standard Deviation:")
print(df.salary.std())

# Statistical description of numerical columns
print("\nStatistical Description:")
print(df.describe())

# Statistical description of all columns
print("\nDescription of All Columns:")
print(df.describe(include='all'))

# Display column names
empCol = df.columns
print("\nEmployee Column Names:")
print(empCol)

# Convert DataFrame into a NumPy array
emparray = df.values
print("\nEmployee NumPy Array:")
print(emparray)

# Convert NumPy array back into a DataFrame
employee_DF = pd.DataFrame(emparray, columns=empCol)
print("\nEmployee DataFrame Created from NumPy Array:")
print(employee_DF)
