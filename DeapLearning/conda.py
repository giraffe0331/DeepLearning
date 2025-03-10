#用anaconda写个数据分析的例子
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建示例数据
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 35, 28, 32],
    '收入': [8000, 12000, 15000, 9000, 13000],
    '工作年限': [2, 5, 8, 3, 6]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 基本统计分析
print("\n基本统计信息：")
print(df.describe())

# 相关性分析
correlation = df[['年龄', '收入', '工作年限']].corr()
print("\n相关性分析：")
print(correlation)

# 数据可视化
plt.figure(figsize=(12, 6))

# 收入分布图
plt.subplot(1, 2, 1)
sns.barplot(x='姓名', y='收入', data=df)
plt.title('各人收入对比')
plt.xticks(rotation=45)

# 工作年限与收入的散点图
plt.subplot(1, 2, 2)
sns.scatterplot(x='工作年限', y='收入', data=df)
plt.title('工作年限与收入关系')

plt.tight_layout()
plt.show()