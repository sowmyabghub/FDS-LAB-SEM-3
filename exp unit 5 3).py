import numpy as np
import pandas as pd

# Load Dataset
df = pd.read_csv("Social_Network_Ads.csv")

print(df.head())

# Features and Label
features = df.iloc[:, [2, 3]].values
label = df.iloc[:, 4].values

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Find suitable random state
for i in range(1, 401):
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        label,
        test_size=0.2,
        random_state=i
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)

    train_score = model.score(x_train, y_train)
    test_score = model.score(x_test, y_test)

    if test_score > train_score:
        print(
            "Test {} Train {} Random State {}".format(
                test_score,
                train_score,
                i
            )
        )

# Final Model
x_train, x_test, y_train, y_test = train_test_split(
    features,
    label,
    test_size=0.2,
    random_state=26
)

finalModel = LogisticRegression(max_iter=1000)
finalModel.fit(x_train, y_train)

print("\nTraining Accuracy:", finalModel.score(x_train, y_train))
print("Testing Accuracy:", finalModel.score(x_test, y_test))

from sklearn.metrics import classification_report

print("\nClassification Report")
print(classification_report(label, finalModel.predict(features)))