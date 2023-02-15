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


y1 = np.array([70, 50, 65, 60, 75, 67, 74])
retrieve_var_value(y1)
y2 = np.array([80, 74, 90, 70, 75, 65, 85])
retrieve_var_value(y2)
y3 = np.array([148, 142, 140, 150, 160, 170, 155])
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

total = np.array([y1, y2, y3])
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
# табличное значение расчитывается как столбец k1 = (k - 1) = 2, ряд k2 = (n - k) = 18
# табличное значение пересечение 2 и 18 - 3.55, а F_n получился 177.48 больше 3.55 значит теория H1 альтернативная
# гипотеза, подтверждает влияние профессии на заработную плату

f = stats.f_oneway(y1, y2, y3)
retrieve_var_value(f)
# F_onewayResult(statistic=177.48291613374704, pvalue=1.4204669001071745e-12)
# это значит что, pvalue гораздо меньше статистического значения, и это гипотиза H1, есть статистически значимые отличия

#POST HOC TEST TUKEY
df = pd.DataFrame({'score': [70, 50, 65, 60, 75, 67, 74,
                             80, 74, 90, 70, 75, 65, 85,
                             148, 142, 140, 150, 160, 170, 155],
                   'group': np.repeat(['accountant', 'lawyer', 'programmer'], repeats=7)})
tukey = pairwise_tukeyhsd(endog=df['score'],
                           groups=df['group'],
                           alpha=0.05)
retrieve_var_value(tukey)

# двухфакторный анализ
# сначала определяется среднее значение в каждой ячейке тут по лекции 4 ячейки
y111 = 57
y112 = 59
y11 = (y111 + y112) / 2
retrieve_var_value(y11)

y121 = 56
y122 = 58
y12 = (y121 + y122) / 2
retrieve_var_value(y12)

y211 = 32
y212 = 34
y21 = (y211 + y212) / 2
retrieve_var_value(y21)

y221 = 71
y222 = 71
y22 = (y221 + y222) / 2
retrieve_var_value(y22)

# затем определяется среднии из уже полученных значений по столбцам и строкам так же 4 значения
YcpA1 = (y11+y12) / 2
retrieve_var_value(YcpA1)
YcpA2 = (y21+y22) / 2
retrieve_var_value(YcpA2)
YcpB1 = (y11+y21) / 2
retrieve_var_value(YcpB1)
YcpB2 = (y12+y22) / 2
retrieve_var_value(YcpB2)

# тут получается среднее из всех средних
Ycp = np.mean(YcpA1 + YcpA2 + YcpB1 + YcpB2) / 4
retrieve_var_value(Ycp)

# каждый элемент возводим в квадрат и суммируем
# первое 2 это количество факторов а
# второе 2 это количество факторов b у нас тоже 2 в лекциях есть таблица 2 на 2
# третье 2 это количество репликаций, тоже 2
SSt = (y111**2 + y112**2 + y121**2 + y122**2 + y211**2 + y212**2 + y221**2 + y222**2) - 2*2*2*(Ycp**2)
retrieve_var_value(SSt)
SSA = 2*2*(YcpA1**2 + YcpA2**2) - 2*2*2*Ycp**2
retrieve_var_value(SSA)
SSB = 2*2*(YcpB1**2 + YcpB2**2) - 2*2*2*Ycp**2
retrieve_var_value(SSB)
SSAB = 2*(y11**2 + y12**2 + y21**2 + y22**2) - 2*2*2*Ycp**2 - SSA - SSB
retrieve_var_value(SSAB)
SSE = SSt - SSA - SSB - SSAB
retrieve_var_value(SSE)

a = 2  # 2 уровня фактора a
и = 2  # 2 уровня фактора b
n = k = 2  # число повторных измерений

dfA = 2-1  # (a - 1)
retrieve_var_value(dfA)
dfB = 2-1  # (b - 1)
retrieve_var_value(dfB)
dfAB = (2-1)*(2-1)  # (a-1)*(b-1)
retrieve_var_value(dfAB)
dfE = 2*2*(2-1)  # a*b*(n-1)
retrieve_var_value(dfE)
MSA = SSA / dfA
retrieve_var_value(MSA)
MSB = SSB / dfB
retrieve_var_value(MSB)
MSAB = SSAB / dfAB
retrieve_var_value(MSAB)
MSE = SSE / dfE
retrieve_var_value(MSE)

FA = MSA / MSE
retrieve_var_value(FA)
FB = MSB / MSE
retrieve_var_value(FB)
FAB = MSAB / MSE
retrieve_var_value(FAB)
#  табличные степени свободы будут k1(числитель) = 1 и k2(знаменатель) = 4 из лекции это пересечение даёт 7.71
F_t = 7.71
# все значения FA, FB, FAB больше табличного F_t

# строим таблицу
fA = np.array(['low', 'low', 'low', 'low', 'high', 'high', 'high', 'high'])
retrieve_var_value(fA)
fB = np.array(['low', 'low', 'high', 'high', 'low', 'low', 'high', 'high'])
retrieve_var_value(fB)
values = np.array([57, 59, 56, 58, 32, 34, 71, 71])
retrieve_var_value(values)
df = pd.DataFrame({'fA': fA, 'fB': fB, 'values': values})
retrieve_var_value(df)
# строим модель с помощью метода ols
lm_model = ols('values ~ C(fA) * C(fB)', data=df).fit()
retrieve_var_value(lm_model)
# строим ANOVA таблицу
table = sm.stats.anova_lm(lm_model, typ=2)
retrieve_var_value(table)