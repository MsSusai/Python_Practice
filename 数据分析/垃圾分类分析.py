# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/7/27  16:18 
# 名称：垃圾分类分析.PY
# 工具：PyCharm
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
from scipy import stats

matplotlib.rcParams['font.family'] = 'SimHei'  # 解决汉字问题
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

# 性别卡平方检验及制图
sexual = pd.read_csv(r"垃圾分类数据/性别.csv")
# print(sexual)
observed = sexual.iloc[0]
expected = sexual.iloc[1]
print("性别卡平方检验结果：" + str(stats.chisquare(f_obs=observed, f_exp=expected)))  # 通过观测值和预测值算卡平方值与p值

sexualLabel = ["男", "女"]
sexualData = [107, 168]
plt.pie(sexualData, labels=sexualLabel, autopct="%.1f%%")
plt.title("性别分布")
plt.savefig(r"C:\Users\sosai\Desktop\性别分布.png", dpi=500, bbox_inches='tight')
plt.close()

# 年龄制图
age = pd.read_csv(r"垃圾分类数据/年龄.csv").squeeze()
# print(age)
age.plot.pie(autopct="%.1f%%", title='年龄分布', explode=(0.1, 0, 0, 0.1, 0, 0.2))
plt.savefig(r"C:\Users\sosai\Desktop\年龄分布.png", dpi=500, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
plt.close()

# 受教育程度制图
background = pd.read_csv(r"垃圾分类数据/受教育程度.csv").squeeze()
# print(background)
background.plot.pie(autopct="%.1f%%", title='受教育程度', explode=(0.2, 0.1, 0, 0, 0.1))
plt.savefig(r"C:\Users\sosai\Desktop\受教育程度.png", dpi=500, bbox_inches='tight')
plt.close()

# 分类认知卡平方及制图
recognize = pd.read_csv(r"垃圾分类数据/分类认知.csv")
print("分类认知卡平方检验结果：" + str(stats.chi2_contingency(recognize)))  # 受高等教育与没受高等教育卡平方
# print(recognize)
right = recognize["正确"].sum()
false = recognize["不正确"].sum()
# print(right, false)

labels = ["正确", "不正确"]
data = [right, false]
plt.pie(data, labels=labels, autopct="%.1f%%", explode=(0, 0.1))
plt.title("分类认知水平")
plt.savefig(r"C:\Users\sosai\Desktop\分类认知.png", dpi=500, bbox_inches='tight')
plt.close()

# 对垃圾分类态度制图
attitude = pd.read_csv(r"垃圾分类数据/对垃圾分类态度.csv").squeeze()
attitude.plot.pie(autopct="%.1f%%", title='垃圾分类态度', explode=(0, 0.1, 0.1))
plt.savefig(r"C:\Users\sosai\Desktop\垃圾分类态度.png", dpi=500, bbox_inches='tight')
plt.close()

# 社区垃圾分类设施
have = pd.read_csv(r"垃圾分类数据/社区垃圾分类设施.csv").squeeze()
have.plot.pie(autopct="%.1f%%", title='社区垃圾分类设施有无', explode=(0, 0.1))
plt.savefig(r"C:\Users\sosai\Desktop\社区垃圾分类设施.png", dpi=500, bbox_inches='tight')
plt.close()

# 垃圾分类信息获取渠道
message = pd.read_csv(r"垃圾分类数据/垃圾分类信息获取渠道.csv").squeeze()
message.plot.pie(autopct="%.1f%%", title='垃圾分类信息获取渠道', explode=(0, 0, 0, 0.1, 0.1, 0))
plt.savefig(r"C:\Users\sosai\Desktop\垃圾分类信息获取渠道.png", dpi=500, bbox_inches='tight')
plt.close()

# 垃圾分类存在问题
question = pd.read_csv(r"垃圾分类数据/垃圾分类存在问题.csv").squeeze()
question.plot.pie(autopct="%.1f%%", title='垃圾分类存在问题', explode=(0, 0, 0.1, 0.1, 0))
plt.savefig(r"C:\Users\sosai\Desktop\垃圾分类存在问题.png", dpi=500, bbox_inches='tight')
plt.close()
