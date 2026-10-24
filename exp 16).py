
# Experiment No: 15
# Experiment to Understand EDA - Quantitative and Qualitative Analysis

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Display first five rows
print("First Five Rows:")
print(tips.head())

# Quantitative Analysis

# 1. Distribution plot
sns.displot(x=tips['total_bill'], kde=True)
plt.show()

sns.displot(x=tips['total_bill'], kde=False)
plt.show()

# 2. Joint plot
sns.jointplot(x=tips['tip'], y=tips['total_bill'])
plt.show()

sns.jointplot(x=tips['tip'], y=tips['total_bill'], kind="reg")
plt.show()

sns.jointplot(x=tips['tip'], y=tips['total_bill'], kind="hex")
plt.show()

# 3. Pair plot
sns.pairplot(tips)
plt.show()

# Qualitative Analysis

# 4. Count of Lunch and Dinner
print("\nTime Value Counts:")
print(tips['time'].value_counts())

sns.pairplot(tips, hue='time')
plt.show()

sns.pairplot(tips, hue='day')
plt.show()

# 5. Heatmap showing correlation
sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.show()

# 6. Box plots
sns.boxplot(x=tips['total_bill'])
plt.show()

sns.boxplot(x=tips['tip'])
plt.show()

# 7. Count plot for days
sns.countplot(x=tips['day'])
plt.show()

# 8. Count plot for gender
sns.countplot(x=tips['sex'])
plt.show()

# 9. Pie chart for gender
tips['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# 10. Bar chart for gender
tips['sex'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.show()

# 11. Count of days during dinner
sns.countplot(x=tips[tips['time'] == 'Dinner']['day'])
plt.title("Days with Dinner")
plt.show()
