
# Experiment No: 13
# Handling Missing and Inappropriate Data in a Dataset
# Using Python Pandas Library

import numpy as np
import pandas as pd

# Create Hotel dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10],
    'Age_Group': [
        '20-25', '30-35', '25-30', '20-25', '35+',
        '35+', '35+', '20-25', '25-30', '25-30', '30-35'
    ],
    'Rating(1-5)': [4, 5, 6, -1, 3, 3, 4, 7, 2, 2, 5],
    'Hotel': [
        'Ibis', 'LemonTree', 'RedFox', 'LemonTree', 'Ibis',
        'Ibys', 'RedFox', 'LemonTree', 'Ibis', 'Ibis', 'RedFox'
    ],
    'FoodPreference': [
        'veg', 'Non-Veg', 'Veg', 'Veg', 'Vegetarian',
        'Non-Veg', 'Vegetarian', 'Veg', 'Non-Veg', 'Non-Veg', 'non-Veg'
    ],
    'Bill': [1300, 2000, 1322, 1234, 989, 1909, 1000, 2999, 3456, 3456, 6755],
    'NoOfPax': [2, 3, 2, 2, 2, 2, -1, -10, 3, 3, 4],
    'EstimatedSalary': [
        40000, 59000, 30000, 120000, 45000, 122220,
        21122, 345673, -99999, -99999, 87777
    ],
    'Age_Group.1': [
        '20-25', '30-35', '25-30', '20-25', '35+',
        '35+', '35+', '20-25', '25-30', '25-30', '30-35'
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Identify duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())

# Display dataset information
print("\nDataset Information:")
df.info()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDataset after Removing Duplicates:")
print(df)

# Count the number of rows
print("\nNumber of Rows:")
print(len(df))

# Reset the index
df.reset_index(drop=True, inplace=True)

print("\nDataset after Resetting Index:")
print(df)

# Remove unnecessary duplicate Age_Group column
df.drop(['Age_Group.1'], axis=1, inplace=True)

# Replace inappropriate negative values with NaN
df.loc[df['CustomerID'] < 0, 'CustomerID'] = np.nan
df.loc[df['Bill'] < 0, 'Bill'] = np.nan
df.loc[df['EstimatedSalary'] < 0, 'EstimatedSalary'] = np.nan

# Handle inappropriate number of people
df.loc[(df['NoOfPax'] < 1) | (df['NoOfPax'] > 20), 'NoOfPax'] = np.nan

# Handle inappropriate ratings outside the range 1 to 5
df.loc[(df['Rating(1-5)'] < 1) | (df['Rating(1-5)'] > 5), 'Rating(1-5)'] = np.nan

print("\nDataset after Replacing Inappropriate Values:")
print(df)

# Display unique age groups and hotels
print("\nUnique Age Groups:")
print(df['Age_Group'].unique())

print("\nUnique Hotels:")
print(df['Hotel'].unique())

# Correct inappropriate hotel name
df['Hotel'] = df['Hotel'].replace({'Ibys': 'Ibis'})

# Standardize food preferences
df['FoodPreference'] = df['FoodPreference'].replace({
    'Vegetarian': 'Veg',
    'veg': 'Veg',
    'non-Veg': 'Non-Veg'
})

print("\nDataset after Correcting Categorical Values:")
print(df)

# Fill missing numerical values
df['EstimatedSalary'] = df['EstimatedSalary'].fillna(
    round(df['EstimatedSalary'].mean())
)

df['NoOfPax'] = df['NoOfPax'].fillna(
    round(df['NoOfPax'].median())
)

df['Rating(1-5)'] = df['Rating(1-5)'].fillna(
    round(df['Rating(1-5)'].median())
)

df['Bill'] = df['Bill'].fillna(
    round(df['Bill'].mean())
)

# Fill missing categorical values using mode
df['Age_Group'] = df['Age_Group'].fillna(
    df['Age_Group'].mode()[0]
)

df['Hotel'] = df['Hotel'].fillna(
    df['Hotel'].mode()[0]
)

df['FoodPreference'] = df['FoodPreference'].fillna(
    df['FoodPreference'].mode()[0]
)

print("\nFinal Cleaned Dataset:")
print(df)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

print("\nFinal Dataset Information:")
df.info()