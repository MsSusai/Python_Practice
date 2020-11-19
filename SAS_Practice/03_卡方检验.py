import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

np.random.seed(12345678)
data = np.random.randint(2, size=(40, 3))  # 2个分类，50个实例，3个特征
data = pd.DataFrame(data, columns=['A', 'B', 'C'])
contingency = pd.crosstab(data['A'], data['B'])  # 建立列联表
print(chi2_contingency(contingency))  # 卡方检验
