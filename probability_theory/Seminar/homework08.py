import numpy as np
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


print('\nДаны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного'
      'скоринга (ks):\n'
      'zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],\n'
      'ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].\n'
      'Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy\n'
      'Полученные значения должны быть равны.\n'
      'Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,\n'
      'а затем с использованием функций из библиотек numpy и pandas.\n')

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
retrieve_var_value(zp)
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
retrieve_var_value(ks)
cov = np.mean(zp * ks) - (np.mean(zp) * np.mean(ks))
retrieve_var_value(cov)
cov_var = np.cov(zp, ks)
retrieve_var_value(cov_var)

# несмещённая коварация
corddof1 = np.cov(zp, ks, ddof=1)
retrieve_var_value(corddof1)

zpstd = np.std(zp, ddof=1)
retrieve_var_value(zpstd)
ksstd = np.std(ks, ddof=1)
retrieve_var_value(ksstd)

nesm_cov = corddof1 / (zpstd * ksstd)
retrieve_var_value(nesm_cov)

# смещённая коварация
corddof0 = np.cov(zp, ks, ddof=0)
retrieve_var_value(corddof0)

zpstd = np.std(zp, ddof=0)
retrieve_var_value(zpstd)
ksstd = np.std(ks, ddof=0)
retrieve_var_value(ksstd)

sm_cov = corddof0 / (zpstd * ksstd)
retrieve_var_value(sm_cov)

spcorrcoef = np.corrcoef(zp, ks)
retrieve_var_value(spcorrcoef)

print('\nИзмерены значения IQ выборки студентов,\n'
      'обучающихся в местных технических вузах:\n'
      '131, 125, 115, 122, 131, 115, 107, 99, 125, 111.\n'
      'Известно, что в генеральной совокупности IQ распределен нормально.\n'
      'Найдите доверительный интервал для математического ожидания с надежностью 0.95.\n')

IQ_izmerennoe = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
IQ = np.mean(IQ_izmerennoe)
retrieve_var_value(IQ)
D2 = np.var(IQ_izmerennoe, ddof=1)
retrieve_var_value(D2)
t2 = stats.t.ppf(0.975, 9)  # 0..975 = это поскольку для интервала мы отсекаем с каждой стороны по 0.025 или 2.5%
# процента для статистической значимости 5%. всего выборка 10, для высчитывания необходимо отнять 1 и того =9
retrieve_var_value(t2)
low_x2 = IQ - t2 * np.sqrt(D2 / 10)
retrieve_var_value(low_x2)
up_x2 = IQ + t2 * np.sqrt(D2 / 10)
retrieve_var_value(up_x2)

print('\nИзвестно, что рост футболистов в сборной распределен нормально\n'
      'с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,\n'
      'среднее выборочное составляет 174.2. Найдите доверительный интервал для математического\n'
      'ожидания с надежностью 0.95.\n')

Z3 = 1.96  # 0.05% берётся со статистической таблицы
retrieve_var_value(Z3)
X3 = 174.2
retrieve_var_value(X3)
N3 = 27
retrieve_var_value(N3)
dispersiya = 25
retrieve_var_value(dispersiya)
Sigma3 = np.sqrt(25) # отклонение корень из 25 незнаю сигма или нет пишется но решил дописать
retrieve_var_value(Sigma3)
low1 = X3 - (Z3 * (Sigma3 / np.sqrt(N3)))
retrieve_var_value(low1)
up1 = X3 + (Z3 * (Sigma3 / np.sqrt(N3)))
retrieve_var_value(up1)
