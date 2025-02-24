import pandas as pd
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt

# 读取并处理数据
df = pd.read_csv("C:\\Users\\24336\\Desktop\\yingxiangyinsu.csv", encoding='GBK')
df = df.apply(pd.to_numeric, errors='coerce')  # 转换为数值，非数值的转换为NaN
df.dropna(inplace=True)  # 删除缺失值
df = (df - df.mean()) / df.std()  # 标准化数据

# 因子分析
fa = FactorAnalyzer(n_factors=5, rotation='varimax', method='principal')
fa.fit(df)

# 获取载荷矩阵和特征值
loadings = fa.loadings_
print("Loadings:\n", loadings)

ev, v = fa.get_eigenvalues()
print("Eigenvalues:", ev)

# 只保留特征值大于1的部分
ev_greater_than_one = ev[ev > 1]
factors_greater_than_one = range(1, len(ev_greater_than_one) + 1)

# 绘制仅显示特征值大于1的图标
plt.figure(figsize=(8, 5))
plt.plot(factors_greater_than_one, ev_greater_than_one, 'o-', label='Eigenvalues > 1', color='#D8BFD8')
plt.title('Scree Plot ')
plt.xlabel('Factors')
plt.ylabel('Eigenvalues')
plt.xticks(factors_greater_than_one)

plt.legend()
plt.grid()
plt.show()

# 获取因子分数
factor_scores = fa.transform(df)
print("Factor Scores:\n", factor_scores)

# 添加因子分数到数据框
for i in range(len(ev_greater_than_one)):
    df[f'Factor{i+1}'] = factor_scores[:, i]

# 保存结果
df.to_csv('factor_scores.csv', index=False)
