# -*- coding: utf-8 -*- 
"""
    Author: 72733
    Datetime: 2024-07-26 15:52
    DESC:
"""


import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd

def heatmap():
# 你的数据
    data = [
        # [0, 0, 0, 7.81, 0, 19.24, 14.43],
        # [0, 0, 0, 20.05, 24.05, 15.43, 12.43],
        # [0, 0, 0, 7.81, 0, 15.43, 18.24],
        # [7.81, 20.05, 7.81, 0, 24.05, 19.24, 4.81],
        # [0, 24.05, 0, 24.05, 0, 0, 0],
        # [19.24, 15.43, 15.43, 19.24, 0, 0, 0],
        # [14.43, 12.43, 18.24, 4.81, 0, 0, 0]
        [0, 0, 0, 8.2, 0, 20.8, 15.6],
        [0, 0, 0, 22.0, 26.0, 16.6, 13.6],
        [0, 0, 0, 8.2, 0, 16.6, 19.8],
        [8.2, 22.0, 8.2, 0, 26.0, 20.8, 5.2],
        [0, 26.0, 0, 26.0, 0, 0, 0],
        [20.8, 16.6, 16.6, 20.8, 0, 0, 0],
        [15.6, 13.6, 19.8, 5.2, 0, 0, 0]
    ]

    # 创建自定义的浅色调颜色映射
    # colors = ['#A398C5', '#7465AD', '#572C92']  # 从浅到深的颜色
    colors = ['#FFFFFF', '#B39EB5']
    n_bins = 256  # 颜色渐变的平滑度
    cmap = LinearSegmentedColormap.from_list("custom", colors, N=n_bins)

    # 行列标签E
    row_labels = ['A:Data Scientist Team', 'A:Innovation sector', 'A:IT sector', 'C: CTO', 'B: Customized services sector', 'B:Algorithm sector', 'B:Engineering sector']
    col_labels = ['A:Data Scientist Team', 'A:Innovation sector', 'A:IT sector', 'C: CTO', 'B: Customized services sector', 'B:Algorithm sector', 'B:Engineering sector']

    # 创建DataFrame
    df = pd.DataFrame(data, index=row_labels, columns=col_labels)

    # 绘制热力图
    plt.figure(figsize=(12, 9))  # 设置图形大小
    # sns.heatmap(df, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True, xticklabels=df.columns, yticklabels=df.index)
    sns.heatmap(df, 
                annot=True,      # 显示数值
                fmt=".2f",       # 数值格式为2位小数
                cmap=cmap,  # 使用紫色系配色
                cbar=True,       # 显示颜色条
                xticklabels=df.columns, 
                yticklabels=df.index)

    # 调整布局
    plt.xticks(rotation=30, ha='right', fontsize=12)  # 旋转x轴标签45度
    plt.yticks(rotation=0, fontsize=12)  # y轴标签水平显示

    # # 更详细的边距控制
    plt.subplots_adjust(left=0.2,    # 增加左边距
                       right=1.05,    # 右边距
                       bottom=0.2,   # 底部边距
                       top=0.95)      # 顶部边距
    
    # plt.tick_params(axis='x', which='both', pad=10)  # 增加刻度标签与轴的距离
    constrained_layout=True
    # 调整子图参数，确保标签不被切掉
    # plt.tight_layout()

    # 显示图形
    plt.show()

if __name__ == "__main__":
    heatmap()