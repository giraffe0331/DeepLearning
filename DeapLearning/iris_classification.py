import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 加载数据集
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 2. 数据预处理
# 标准化特征
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

# 3. 模型训练
# 使用支持向量机(SVM)分类器
svm = SVC(kernel='rbf', random_state=42)
svm.fit(X_train, y_train)

# 4. 模型评估
# 使用交叉验证评估模型
cv_scores = cross_val_score(svm, X_scaled, y, cv=5)
print('\n交叉验证分数：')
print(f'平均准确率: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})')

# 在测试集上进行预测
y_pred = svm.predict(X_test)

# 打印分类报告
print('\n分类报告：')
print(classification_report(y_test, y_pred, target_names=target_names))

# 5. 可视化分析
plt.figure(figsize=(15, 10))

# 5.1 混淆矩阵热图
plt.subplot(2, 2, 1)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=target_names,
            yticklabels=target_names)
plt.title('混淆矩阵')
plt.xlabel('预测标签')
plt.ylabel('真实标签')

# 5.2 特征分布图
plt.subplot(2, 2, 2)
for i in range(3):
    sns.kdeplot(data=X[y == i, 0], label=target_names[i])
plt.title('萼片长度分布')
plt.xlabel('萼片长度 (cm)')
plt.ylabel('密度')
plt.legend()

# 5.3 特征散点图
plt.subplot(2, 2, 3)
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=target_names[y],
                style=target_names[y], s=100)
plt.title('萼片长度 vs 萼片宽度')
plt.xlabel('萼片长度 (cm)')
plt.ylabel('萼片宽度 (cm)')

# 5.4 箱线图
plt.subplot(2, 2, 4)
df = pd.DataFrame(X, columns=feature_names)
df['target'] = pd.Categorical.from_codes(y, target_names)
df_melted = pd.melt(df, id_vars=['target'])
sns.boxplot(x='variable', y='value', hue='target', data=df_melted)
plt.title('特征箱线图')
plt.xticks(rotation=45)

# 调整布局并显示图形
plt.tight_layout()
plt.show()