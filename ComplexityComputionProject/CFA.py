import pandas as pd
from semopy import Model, calc_stats
import numpy as np

# 读取数据，处理缺失值和标准化
df = pd.read_csv("C:\\Users\\24336\\Desktop\\yingxiangyinsu.csv", encoding='GBK')
df = df.apply(pd.to_numeric, errors='coerce')  # 转换为数值，非数值的转换为 NaN
df = df.dropna()  # 删除包含 NaN 的行
df = (df - df.mean()) / df.std()  # 数据标准化

# 优化后的 CFA 测量模型
model_desc_optimized = """
# 优化后的模型定义

#Factor1 =~ V5 + V8 + V9

Factor2 =~ V11 + V12
Factor3 =~ V15 + V13 + V14
Factor4 =~ V3 + V4

# 增加潜变量间协方差

 #Factor1 ~~ Factor2
 #Factor1 ~~ Factor3

Factor2 ~~ Factor3

 #Factor4 ~~ Factor1

Factor4 ~~ Factor2
Factor4 ~~ Factor3
"""

# 创建 semopy 模型
model_optimized = Model(model_desc_optimized)

# 拟合优化后的模型
model_optimized.fit(df)

# 输出拟合结果
parameters_optimized = model_optimized.inspect()
print("优化后的模型参数估计：\n", parameters_optimized)
print(parameters_optimized[['lval', 'rval', 'Estimate']])

# 计算 AVE 和 CR 的函数
def calculate_AVE_CR(parameters, threshold=0.3):
    ave_cr = {}
    for factor in parameters['lval'].unique():
        if 'Factor' not in factor:
            continue
        factor_params = parameters[(parameters['lval'] == factor) & (parameters['Estimate'] >= threshold)]
        if factor_params.empty:
            continue
        # AVE
        lambda_sq_sum = (factor_params['Estimate'] ** 2).sum()
        ave = lambda_sq_sum / len(factor_params)
        # CR
        lambda_sum = factor_params['Estimate'].sum()
        theta_sum = (factor_params['Std. Err'] ** 2).sum()
        cr = (lambda_sum ** 2) / (lambda_sum ** 2 + theta_sum)
        ave_cr[factor] = {'AVE': ave, 'CR': cr}
    return ave_cr

# 计算并输出优化后的 AVE 和 CR
ave_cr_optimized = calculate_AVE_CR(parameters_optimized)
print("优化后的 AVE 和 CR 指标：")
for factor, values in ave_cr_optimized.items():
    print(f"{factor}: AVE = {values['AVE']:.4f}, CR = {values['CR']:.4f}")

# 模型拟合统计指标
stats_optimized = calc_stats(model_optimized)
print("优化后的模型拟合统计指标：")
print(stats_optimized)


# 提取 CFI, TLI 和 RMSEA
try:
    cfi = stats_optimized.loc['Value', 'CFI']
    tli = stats_optimized.loc['Value', 'TLI']
    rmsea = stats_optimized.loc['Value', 'RMSEA']

    # 打印结果
    print(f"CFI: {cfi:.4f}")
    print(f"TLI: {tli:.4f}")
    print(f"RMSEA: {rmsea:.4f}")
except KeyError as e:
    print(f"无法找到指定的列或行：{e}")

# 可视化路径图（需要 graphviz 库）
try:
    from semopy.plotter import plot_model

    plot_model(model_optimized, "cfa_model_optimized.png")
    print("路径图已保存为 cfa_model_optimized.png")
except ImportError:
    print("Graphviz 未安装，跳过路径图生成。")
