import numpy as np
from scipy import stats
mother_heights = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169])
daughter_heights = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])
answer = stats.ttest_rel(mother_heights, daughter_heights)
print('4 function= ', answer)
new_answer = (np.mean(mother_heights) - np.mean(daughter_heights)) / (
    np.sqrt((np.var(mother_heights, ddof=1) / len(mother_heights)) +
            (np.var(daughter_heights, ddof=1) / len(daughter_heights))))
print('4 hand?= ', new_answer)

vendor_true = 200
cookies_weights = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
medium_c_w = np.mean(cookies_weights)
print('3 medium_c_w= ', medium_c_w)
std_c_w = np.std(cookies_weights, ddof=1)
print('3 std_c_w= ', std_c_w)
t = (medium_c_w - vendor_true) / (std_c_w / np.sqrt(len(cookies_weights)))
print('3 t= ', t)
print('3 t tablica pri 99%= 3.24983554402')
print('3 test_1samp=', stats.ttest_1samp(cookies_weights, 10))

a = 0.05
n = 100
dispersiya = 4
zr = (17.5-17) / (dispersiya / np.sqrt(n))
print('2 zr= ', zr)
print('2 z tablica=', 0.89435)
