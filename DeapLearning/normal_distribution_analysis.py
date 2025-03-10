import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 生成正态分布数据
np.random.seed(42)  # 设置随机种子以确保结果可重现
data = np.random.normal(loc=0, scale=1, size=1000)  # 生成均值为0，标准差为1的正态分布数据

# 创建一个2x2的子图布局
plt.figure(figsize=(12, 10))

# 1. 直方图和密度曲线
plt.subplot(2, 2, 1)
sns.histplot(data=data, kde=True)
plt.title('正态分布直方图和密度曲线')
plt.xlabel('值')
plt.ylabel('频数')

# 2. Q-Q图
plt.subplot(2, 2, 2)
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q图')

# 3. 箱线图
plt.subplot(2, 2, 3)
sns.boxplot(data=data)
plt.title('箱线图')

# 4. 小提琴图
plt.subplot(2, 2, 4)
sns.violinplot(data=data)
plt.title('小提琴图')

# 调整子图布局
plt.tight_layout()

# 计算并显示统计指标
mean = np.mean(data)
std = np.std(data)
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# 打印统计信息
print('\n统计指标分析：')
print(f'均值: {mean:.4f}')
print(f'标准差: {std:.4f}')
print(f'偏度: {skewness:.4f}')
print(f'峰度: {kurtosis:.4f}')

# 显示图形
plt.show()