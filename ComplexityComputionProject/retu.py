import pandas as pd
from semopy import Model
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# 读取数据，处理缺失值和标准化
df = pd.read_csv("C:\\Users\\24336\\Desktop\\yingxiangyinsu.csv", encoding='GBK')
df = df.apply(pd.to_numeric, errors='coerce')  # 转换为数值，非数值的转换为 NaN
df = df.dropna()  # 删除包含 NaN 的行
df = (df - df.mean()) / df.std()  # 数据标准化

# 优化后的 CFA 测量模型
model_desc_optimized = """
# 优化后的模型定义
Organizational_structures =~ V12 + V11
Requirement_analsis_and_technology =~ V15 + V13 + V14
Communication =~ V3 + V4

# 增加潜变量间协方差
Organizational_structures ~~ Requirement_analsis_and_technology
Communication ~~ Organizational_structures
Communication ~~ Requirement_analsis_and_technology
"""

# 创建 semopy 模型
model_optimized = Model(model_desc_optimized)

# 拟合优化后的模型
model_optimized.fit(df)

# 提取因子得分
factor_scores = model_optimized.predict_factors(df)

# 计算三个因子之间的相关性矩阵
factor_correlation = factor_scores[['Organizational_structures', 'Requirement_analsis_and_technology', 'Communication']].corr()

# 自定义浅紫色颜色映射
custom_cmap = mcolors.LinearSegmentedColormap.from_list(
    "custom_cmap",
    ['#FFFFFF', '#B39EB5'],  # 从白色到浅紫色
    N=256  # 渐变颜色数量
)

# 绘制热图，使用自定义颜色映射
plt.figure(figsize=(8, 6))
sns.heatmap(
    factor_correlation,
    annot=True,
    cmap=custom_cmap,  # 使用自定义颜色映射
    fmt='.2f',
    vmin=-1,
    vmax=1,
    annot_kws={'ha': 'center', 'va': 'center', 'fontsize': 11}  # 格子内注释居中，调整字体大小
)

# 调整布局
plt.xticks(rotation=30, ha='right', fontsize=11)  # 旋转x轴标签30度，右对齐
plt.yticks(rotation=0, fontsize=11)  # y轴标签水平显示

# 更详细的边距控制
plt.subplots_adjust(left=0.40, right=1.0, bottom=0.35, top=0.90)  # 调整边距

# 标题居中
plt.title('Correlation Matrix of Three Factors', ha='center', fontsize=14)

# 保存和显示图像
plt.savefig("factor_correlation_matrix_custom.png", bbox_inches='tight')  # 保存图像时确保标签完整
plt.show()

print("相关矩阵热图已保存为 factor_correlation_matrix_custom.png")