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
f = stats.f_oneway(y1, y2, y3)
retrieve_var_value(f)

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
retrieve_var_value(y1)
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184])
retrieve_var_value(y2)
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177])
retrieve_var_value(y3)
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
