from scipy import stats
import numpy as np

np.random.seed(12345678)
rvs = stats.norm.rvs(loc=5, scale=10, size=(100, 2))
print(stats.ttest_1samp(rvs, [1, 5]))
