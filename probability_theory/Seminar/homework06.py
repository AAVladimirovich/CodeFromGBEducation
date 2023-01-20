import numpy as np
from scipy import stats
from varname import nameof
import inspect

def retrieve_name(var):
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


Z1 = 1.96  # 0.05%
retrieve_name(Z1)

X1 = 80
retrieve_name(X1)
N1 = 256
retrieve_name(N1)
Sigma1 = 16
retrieve_name(Sigma1)

low1 = X1 + (Z1* (Sigma1/np.sqrt(N1)))
retrieve_name(low1)

up1 = X1 - (Z1* (Sigma1/np.sqrt(N1)))
retrieve_name(up1)

X2_izmerennoe = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
X2 = np.mean(X2_izmerennoe)
retrieve_name(X2)

D2 = np.var(X2_izmerennoe, ddof=1)
retrieve_name(D2)

t2 = stats.t.ppf(0.975, 9)
retrieve_name(t2)

low_x2 = X2 - t2 * np.sqrt(D2/10)
retrieve_name(low_x2)

up_x2 = X2 + t2 * np.sqrt(D2/10)
retrieve_name(up_x2)


daughter_height = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
retrieve_name(daughter_height)
mother_height = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
retrieve_name(mother_height)

X31 = np.mean(daughter_height)
retrieve_name(X31)
X32 = np.mean(mother_height)
retrieve_name(X32)
delta = X31 - X32
retrieve_name(delta)

D31 = np.var(daughter_height, ddof=1)
retrieve_name(D31)

D32 = np.var(mother_height, ddof=1)
retrieve_name(D32)

D3 = (D31 + D32) / 2
retrieve_name(D3)

SE3 = np.sqrt(D3/10 + D3/10)
retrieve_name(SE3)

t3 = stats.t.ppf(0.975, 18)
retrieve_name(t3)

low3 = delta - t3 * SE3
retrieve_name(low3)

up3 = delta + t3 * SE3
retrieve_name(up3)
