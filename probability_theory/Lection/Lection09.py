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

s = np.array([27, 37, 42, 48, 57, 56, 77, 80])
retrieve_var_value(s)
p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
retrieve_var_value(p)
n = 8
retrieve_var_value(n)

b1 = (n * np.sum(p*s) - np.sum(s) * np.sum(p)) / (n*np.sum(s**2)-np.sum(s)**2)
retrieve_var_value(b1)

b1 = (np.mean(s*p) - np.mean(s) * np.mean(p)) / (np.mean(s**2) - np.mean(s)**2)
retrieve_var_value(b1)

b0 = np.mean(p) - b1 * np.mean(s)
retrieve_var_value(b0)

y_pred = b0 + b1 * s
retrieve_var_value(y_pred)


mse = ((p-y_pred)**2).sum()/n
retrieve_var_value(mse)

x = s.reshape((8, 1))
retrieve_var_value(x)

y = p.reshape((8, 1))
retrieve_var_value(y)

X = np.hstack([np.ones((8, 1)), x])
retrieve_var_value(X)

B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
retrieve_var_value(B)

def mse_(B1, y = y, x = x, n = 8):
    return np.sum((B1*x - y) ** 2) / n

alpha = 1e-6
retrieve_var_value(alpha)

#mse = 1/n * np.sum((B1*x - y) **2 )
#mse = (2/n) * np.sum((B1*X - y) * X )

B1 = 0.1
retrieve_var_value(B1)
n = 8
retrieve_var_value(n)

for i in range (10):
    B1 -= alpha * (2/n) * np.sum((B1*x-y)*x)
    print('B1 = {}'.format(B1))


for i in range (3000):
    B1 -= alpha * (2/n) * np.sum((B1*x-y)*x)
    if i % 500 == 0:
        print('Iteration = {i}, B1 = {B1}, mse = {mse}'.format(i=i, B1=B1, mse=mse_(B1)))


mse = mse_(0.041668015587382985)
retrieve_var_value(mse)


model = LinearRegression()

s = s.reshape(-1, 1)
retrieve_var_value(s)

regres = model.fit(s, p)
retrieve_var_value(regres)

print(regres.intercept_)
print(regres.coef_)

y_pred = model.predict(s)
retrieve_var_value(y_pred)

df = pd.DataFrame({'real': p, 'predicted': y_pred})
retrieve_var_value(df)

#r = np.corrcoef(s, p)
#retrieve_var_value(r)

#retrieve_var_value(r**2)

#regres.score(s, p)

stats.f.ppf(1-0.05, 1, 6)

# критерий Фишера F = Msf / Mso
# в свою очередь Msf (фактическая сумма квадратных отклонений на одну степень свободы)
# Msf = SSf / df1

# остаточная сумма квадратных отлонений на 1 степень свободны
# Mso = SSo / df2

# df1 - степени свободны числителя df1 = p -1, где p - число параметров ( у нас площадь и цена, т.е. 2)
# df2 - степень свободны знаменателя df2 = n - p, где n - число парных измерений ( у нас n = 8 )

# SSf - сумма квадратных отклонений фактическая
# SSo - сумма квадратных отклонений остаточная


df1 = 2 - 1
df2 = 8 - 2

SSf = sum((y_pred - np.mean(p)**2))
SSo = np.sum((p - y_pred)**2)
Msf = SSf/ df1
Mso = SSo/ df2
F = Msf / Mso

stats.t.ppf(1-0.025, 6)

sb = np.sqrt( Mso / np.sum((s-np.mean(s))**2))
retrieve_var_value(sb)

s0 = np.sqrt((Mso * np.sum(s**2))/(n * np.sum((s - np.mean(s))**2)))
retrieve_var_value(s0)

tb = b1 / sb # критерий стьюдента для коэффициента b1
retrieve_var_value(tb)

t0 = b0 / s0 # критерий Стьюдента для коэффициента b0
retrieve_var_value(t0)

stats.t.ppf(1-0.025, 6)






























