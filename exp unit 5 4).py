print("START")

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target

xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(xtrain, ytrain)

print("Training Accuracy:", model.score(xtrain, ytrain))
print("Testing Accuracy:", model.score(xtest, ytest))

print("END")