import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from scipy import stats
import inspect
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm
from statsmodels.formula.api import ols


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


y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
retrieve_var_value(y1)
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
retrieve_var_value(y2)
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
retrieve_var_value(y3)

k = 3  # количество групп
retrieve_var_value(k)
n = len(y1) + len(y2) + len(y3)
retrieve_var_value(n)

y_mean1 = np.mean(y1)  # cреднее значение для y1
retrieve_var_value(y_mean1)
y_mean2 = np.mean(y2)  # cреднее значение для y2
retrieve_var_value(y_mean2)
y_mean3 = np.mean(y3)  # cреднее значение для y3
retrieve_var_value(y_mean3)

total = y1
total = np.append(total, y2)
total = np.append(total, y3)
retrieve_var_value(total)
y_mean_total = np.mean(total)
retrieve_var_value(y_mean_total)

sumsqr_total = np.sum((total - y_mean_total) ** 2)  # сумма квадратов отклонений наблюдений от общего среднего
retrieve_var_value(sumsqr_total)

S_f = np.sum((y_mean1 - y_mean_total) ** 2) * len(y1) + np.sum((y_mean2 - y_mean_total) ** 2) * len(y2) + np.sum(
    (y_mean3 - y_mean_total) ** 2) * len(y3)
retrieve_var_value(S_f)  # сумма квадратов отклонений средних групповых значений от общего среднего

S_ost = np.sum((y1 - y_mean1) ** 2) + np.sum((y2 - y_mean2) ** 2) + np.sum((y3 - y_mean3) ** 2)
retrieve_var_value(S_ost)  # остаточная сумма квадратов отклонений

D_f = S_f / (k - 1)
retrieve_var_value(D_f)  # факторная дисперсия
D_ost = S_ost / (n - k)
retrieve_var_value(D_ost)  # остаточная дисперсия
F_n = D_f / D_ost
retrieve_var_value(F_n)  # наблюдаемый критерий фишера
# табличное значение расчитывается как столбец k1 = (k - 1) = 2, ряд k2 = (n - k) = 25
# табличное значение пересечение 2 и 25 = 5.57, а F_n получился 5.5 меньше 5.57 значит гипотеза H0
# гипотеза, подтверждает отсутствие ститистически значимых различий на рост


f = stats.f_oneway(y1, y2, y3)
retrieve_var_value(f)


# POST HOC TEST TUKEY
df = pd.DataFrame({'heights': [173, 175, 180, 178, 177, 185, 183, 182,
                               177, 179, 180, 188, 177, 172, 171, 184,
                               172, 173, 169, 177, 166, 180, 178, 177],
                   'group': np.repeat(['Футболисты', 'Хоккеисты', 'Штангисты'], repeats=8)})
tukey = pairwise_tukeyhsd(endog=df['heights'],
                          groups=df['group'],
                          alpha=0.05)
retrieve_var_value(tukey)
