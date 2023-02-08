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

s = np.array([27, 37, 42, 48, 57, 56, 77, 80])
retrieve_var_value(s)
p = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
retrieve_var_value(p)
plt.scatter(s, p)
plt.show()


x = np.array([0, -1, 1, -2, 2, -3, 3, -4, 4])
retrieve_var_value(x)

y = x**2
retrieve_var_value(y)

corrcoef = np.corrcoef(x, y)
retrieve_var_value(corrcoef)

plt.scatter(x, y)
plt.show()

a = np.array([1, 2, 3, 4, 5])
retrieve_var_value(a)

b = np.array([7, 4, 6, 9, 0])
retrieve_var_value(b)
abcorrcoef = np.corrcoef(a, b)
retrieve_var_value(abcorrcoef)

b = np.array([11, 12, 0.8, 9, 0.4])
retrieve_var_value(b)
abcorrcoef = np.corrcoef(a, b)
retrieve_var_value(abcorrcoef)

b = np.array([0.5, 0.7, 0.9, 0.8, 1])
retrieve_var_value(b)
abcorrcoef = np.corrcoef(a, b)
retrieve_var_value(abcorrcoef)


p = np.array([27, 37, 42, 48, 57, 56, 77, 80])
retrieve_var_value(p)
s = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
retrieve_var_value(s)
cov = np.mean(p*s) - np.mean(p) * np.mean(s)
retrieve_var_value(cov)
cov_var = np.cov(p, s)
retrieve_var_value(cov_var)

#несмещённая коварация
corddof1 = np.cov(p, s, ddof=1)
retrieve_var_value(corddof1)

sstd = np.std(s, ddof=1)
retrieve_var_value(sstd)
pstd = np.std(p, ddof=1)
retrieve_var_value(pstd)

nesm_cov = corddof1 / (pstd * sstd)
retrieve_var_value(nesm_cov)

#смещённая коварация
corddof0 = np.cov(p, s, ddof=0)
retrieve_var_value(corddof0)

sstd = np.std(s, ddof=0)
retrieve_var_value(sstd)
pstd = np.std(p, ddof=0)
retrieve_var_value(pstd)

sm_cov = corddof0 / (pstd * sstd)
retrieve_var_value(sm_cov)

spcorrcoef = np.corrcoef(p, s)
retrieve_var_value(spcorrcoef)


p = np.array([27, 37, 42, 48, 57, 56, 77, 80])
retrieve_var_value(p)
s = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
retrieve_var_value(s)

spearmanr = stats.spearmanr(p, s)
retrieve_var_value(spearmanr)

p = np.array([27, 37, 42, 48, 57, 56, 77, 80])
retrieve_var_value(p)
p2 = np.array([1, 2, 3.5, 3.5, 6, 5, 7, 8])
retrieve_var_value(p2)
s = np.array([1.2, 1.6, 1.8, 1.8, 2.5, 2.6, 3, 3.3])
retrieve_var_value(s)
s2 = np.array([1, 2, 3, 4, 6, 5, 7, 8])
retrieve_var_value(s2)

s2p2corr = np.corrcoef(s2, p2)
retrieve_var_value(s2p2corr)


































