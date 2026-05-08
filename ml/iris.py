# The Iris dataset is referred to as a "toy dataset" because it has only 150 samples and four features.
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris
# virginica. Each sample's features are the sepal length, sepal width, petal
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower
# that protect the smaller inside petals before the flower buds bloom.

from sklearn.datasets import load_iris

#EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up
iris = load_iris()

# display the shape of the data, target and target_names
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    iris.data, iris.target, random_state=11
)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train)

predicted = knn.predict(X=data_test)
expected = target_test

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)
print("Predicted:", [iris.target_names[p] for p in predicted[:10]])
print("Expected: ", [iris.target_names[e] for e in expected[:10]])

# display the values that the model got wrong
wrong = [(iris.target_names[p], iris.target_names[e])
         for (p, e) in zip(predicted, expected) if p != e]
print(f"\nWrong predictions: {wrong}")
print(f"Accuracy Score: {knn.score(data_test, target_test):.2%}")

# visualize the data using the confusion matrix
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
confusion_df = pd.DataFrame(confusion,
                            index=iris.target_names,
                            columns=iris.target_names)

figure, axes = plt.subplots(figsize=(7, 6))
sns.heatmap(confusion_df, annot=True, cmap="nipy_spectral_r", ax=axes)
axes.set_xlabel("Expected")
axes.set_ylabel("Predicted")
plt.tight_layout()
plt.show()
