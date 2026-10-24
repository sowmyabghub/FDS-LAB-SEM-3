
# Experiment No: 9
# Matplotlib Library Use Cases in Data Science through Visualization
# Dataset: Iris Dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset automatically
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

# Rename columns to match the experiment
data.columns = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm',
    'variety'
]

# Add ID column
data.insert(0, 'Id', range(1, len(data) + 1))

# Display dataset
print(data)

# Display dataset information
data.info()

# Statistical description
print(data.describe())

# Count each Iris variety
print(data.value_counts('variety'))

# Count plot
sns.countplot(x='variety', data=data)
plt.title('Count of Iris Varieties')
plt.show()

# Convert categorical data into dummy variables
dummies = pd.get_dummies(data['variety'])

FinalDataset = pd.concat(
    [dummies, data.iloc[:, [0, 1, 2, 3]]],
    axis=1
)

print(FinalDataset.head())

# Scatter plot: Sepal Length vs Sepal Width
sns.scatterplot(
    x='SepalLengthCm',
    y='SepalWidthCm',
    hue='variety',
    data=data
)
plt.title('Sepal Length vs Sepal Width')
plt.show()

# Scatter plot: Petal Length vs Petal Width
sns.scatterplot(
    x='PetalLengthCm',
    y='PetalWidthCm',
    hue='variety',
    data=data
)
plt.title('Petal Length vs Petal Width')
plt.show()

# Pair plot
sns.pairplot(data, hue='variety', height=3)
plt.show()

# Histogram: Petal Length
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'PetalLengthCm'
).add_legend()
plt.show()

# Histogram: Petal Width
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'PetalWidthCm'
).add_legend()
plt.show()

# Histogram: Sepal Length
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'SepalLengthCm'
).add_legend()
plt.show()

# Histogram: Sepal Width
sns.FacetGrid(data, hue='variety', height=5).map(
    sns.histplot, 'SepalWidthCm'
).add_legend()
plt.show()