from sklearn.datasets import load_digits

digits = load_digits()

print(digits.DESCR)

print(digits.data[13])
print(digits.data.shape)

print(digits.target[13])
print(digits.target.shape) #target just shows rows

import matplotlib.pyplot as plt
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
    
for item in zip(axes.ravel(), digits.images, digits.target):
    axes,image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()
plt.show()

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    digits.data, digits.target, random_state=11
)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train) #Training happens here #This is where the model learns from the data, and the target is what it is trying to predict

predicted = knn.predict(X=data_test)
print(predicted[:20])

expected = target_test
print(expected[:20])

wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]

#print(wrong)

print(f"Accuracy Score: {knn.score(data_test, target_test):.2%}")

#more samples and more features the more accurate the model will be, but it will also take more time to train and predict.

from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)

import pandas as pd
import seaborn as sns

confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
figure, axes = plt.subplots(figsize=(7, 6))
sns.heatmap(confusion_df, annot=True, cmap="nipy_spectral_r", ax=axes)
axes.set_xlabel("Expected")
axes.set_ylabel("Predicted")
plt.tight_layout()
plt.show()