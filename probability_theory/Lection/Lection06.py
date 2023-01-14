import numpy as np
from scipy import stats
from varname import nameof


person_heights = np.array([178, 184, 149, 193, 186, 173, 169, 175, 159, 174])
x_1 = np.mean(person_heights)
print(nameof(x_1), '=', x_1)

D1 = np.var(person_heights, ddof=1)
print(nameof(D1), '=', D1)

t1 = stats.t.ppf(0.975, 9)
print(nameof(t1), '=', t1)

min_x1 = x_1 - t1 * np.sqrt(D1/10)
print(nameof(min_x1), '=', min_x1)

max_x1 = x_1 + t1 * np.sqrt(D1/10)
print(nameof(max_x1), '=', max_x1)


ap_height = np.array([178, 184, 149, 193, 186, 173, 169, 175, 159, 174])
print(nameof(ap_height), '=', ap_height)
bp_height = np.array([150, 154, 167, 165, 171, 150, 158, 170, 175, 160])
print(nameof(bp_height), '=', bp_height)

x_11 = np.mean(ap_height)
print(nameof(x_11), '=', x_11)
x_22 = np.mean(bp_height)
print(nameof(x_22), '=', x_22)
delta = x_11 - x_22
print(nameof(delta), '=', delta)

D11 = np.var(ap_height, ddof=1)
print(nameof(D11), '=', D11)

D22 = np.var(bp_height, ddof=1)
print(nameof(D22), '=', D22)

D = (D11 + D22) / 2
print(nameof(D), '=', D)

SE = np.sqrt(D/10 + D/10)
print(nameof(SE), '=', SE)

t = stats.t.ppf(0.975, 18)
print(nameof(t), '=', t)

low = delta - t * SE
print(nameof(low), '=', low)

upper = delta + t * SE
print(nameof(upper), '=', upper)

