
# Experiment No: 15
# Experiment to Understand Data Preprocessing in Data Science

import numpy as np
import pandas as pd

# Create the dataset
data = {
    'Country': [
        'France', 'Spain', 'Germany', 'Spain', 'Germany',
        'France', 'Spain', 'France', np.nan, 'France'
    ],
    'Age': [44, 27, 30, 38, 40, 35, np.nan, 48, 50, 37],
    'Salary': [
        72000, 48000, 54000, 61000, np.nan,
        58000, 52000, 79000, 83000, 67000
    ],
    'Purchased': [
        'No', 'Yes', 'No', 'No', 'Yes',
        'Yes', 'No', 'Yes', 'No', 'Yes'
    ]
}

df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)

# Display dataset information
print("\nDataset Information:")
df.info()

# Find the mode of Country
print("\nMode of Country:")
print(df['Country'].mode())

print("\nFirst Mode Value:")
print(df['Country'].mode()[0])

# Handle missing values
df['Country'] = df['Country'].fillna(df['Country'].mode()[0])

df['Age'] = df['Age'].fillna(df['Age'].median())

df['Salary'] = df['Salary'].fillna(round(df['Salary'].mean()))

# Display dataset after handling missing values
print("\nDataset After Handling Missing Values:")
print(df)

# Convert Country categorical data into dummy variables
print("\nDummy Variables:")
print(pd.get_dummies(df['Country']))

# Create updated dataset using one-hot encoding
updated_dataset = pd.concat(
    [
        pd.get_dummies(df['Country']),
        df[['Age', 'Salary', 'Purchased']]
    ],
    axis=1
)

# Display updated dataset
print("\nUpdated Dataset:")
print(updated_dataset)

# Convert Purchased values into numerical values
updated_dataset['Purchased'] = updated_dataset['Purchased'].replace({
    'No': 0,
    'Yes': 1
})

# Display final preprocessed dataset
print("\nFinal Preprocessed Dataset:")
print(updated_dataset)

# Display original dataset information
print("\nOriginal Dataset Information After Preprocessing:")
df.info()
