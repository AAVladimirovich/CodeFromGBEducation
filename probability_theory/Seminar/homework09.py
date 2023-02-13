import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy import stats
import inspect
import matplotlib.pyplot as plt

def retrieve_var_value(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            # return names[0]
            print(names[0], '=', var)
            break


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
retrieve_var_value(zp)
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
retrieve_var_value(ks)


corrcoef = np.corrcoef(zp, ks)
retrieve_var_value(corrcoef)
print(f"коэффициент детерминации =  {corrcoef**2}")


x = zp
y = ks
n = len(zp)
b1 = (n * np.sum(x*y) - np.sum(x) * np.sum(y)) / (n*np.sum(x**2)-np.sum(x)**2)
retrieve_var_value(b1)
b0 = np.mean(y) - b1 * np.mean(x)
retrieve_var_value(b0)
y_pred = b0 + b1 * x
retrieve_var_value(y_pred)

mse = ((y-y_pred)**2).sum()/n
retrieve_var_value(mse)

plt.scatter(zp, ks)
plt.plot(zp, y_pred)
plt.title("посчитаем график")
plt.xlabel('zp')
plt.ylabel('ks')
plt.show()

model = LinearRegression()
x = x.reshape(-1, 1)
retrieve_var_value(x)
regres = model.fit(x, y)
retrieve_var_value(regres)
print(f"intercept = {regres.intercept_}")
print(f"slope? = {regres.coef_}")

df = pd.DataFrame({'real': y, 'predicted': y_pred})
retrieve_var_value(df)




zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
retrieve_var_value(zp)
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
retrieve_var_value(ks)

x = zp.reshape((10, 1))
retrieve_var_value(x)

y = ks.reshape((10, 1))
retrieve_var_value(y)

X = np.hstack([np.ones((10, 1)), x])
retrieve_var_value(X)

B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
retrieve_var_value(B)

def mse_(B1, y = y, x = x, n = 10):
    return np.sum((B1*x - y) ** 2) / n

alpha = 1e-6
retrieve_var_value(alpha)
B1 = 0.1
retrieve_var_value(B1)
retrieve_var_value(n)

for i in range (10):
    B1 -= alpha * (2/n) * np.sum((B1*x-y)*x)
    print('B1 = {}'.format(B1))


for i in range (3001):
    B1 -= alpha * (2/n) * np.sum((B1*x-y)*x)
    if i % 500 == 0:
        print('Iteration = {i}, B1 = {B1}, mse = {mse}'.format(i=i, B1=B1, mse=mse_(B1)))