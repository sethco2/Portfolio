''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

# Load the dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

#how many sameples and How many features?
print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}")

# What does feature s6 represent?
# s6 represents a blood serum measurement (blood glucose level), one of six serum measurements
print("Feature s6 represents: blood glucose level (a serum measurement)")

# Use s6 (index 9) as the single feature for regression
X_s6 = X[:, 9].reshape(-1, 1)

# Fit linear regression model
model = LinearRegression()
model.fit(X_s6, y)

#print out the coefficient
print(f"Coefficient: {model.coef_[0]:.4f}")

#print out the intercept
print(f"Intercept: {model.intercept_:.4f}")

# create a scatterplot with regression line
plt.scatter(X_s6, y, color='steelblue', alpha=0.5, label='Data points')
x_line = np.linspace(X_s6.min(), X_s6.max(), 100).reshape(-1, 1)
plt.plot(x_line, model.predict(x_line), color='red', linewidth=2, label='Regression line')
plt.xlabel('s6 (Blood Glucose Level)')
plt.ylabel('Disease Progression')
plt.title('Diabetes Dataset: s6 vs Disease Progression')
plt.legend()
plt.tight_layout()
plt.savefig('diabetes_regression.png')
print("Plot saved to diabetes_regression.png")