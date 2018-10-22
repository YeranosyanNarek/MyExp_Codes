import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("/home/yeranosyan/ML/notebooks/Advertising.csv")
#print(df.head())
#df.plot.scatter(x="TV", y="sales")

x = np.array(df[["TV", "radio", "newspaper"]])
y = np.array(df.sales)
print(x.shape, y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.45, random_state=20)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Create linear regression object
lin_reg = linear_model.LinearRegression()

# Train the model using the training sets
lin_reg.fit(x_train, y_train)

# Make predictions using the testing set
y_pred = lin_reg.predict(x_test)

# The coefficients
print('Coefficients: \n', lin_reg.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_pred, y_test))

# Plot outputs
plt.scatter(x_test[:, 0], y_test,  color='red')

x = np.linspace(min(x_test[:, 0]), max(x_test[:, 0]), 100)
plt.plot(x, lin_reg.intercept_ + lin_reg.coef_[0]*x, color='black', linewidth=3)
plt.xticks(())
plt.yticks(())

plt.show()