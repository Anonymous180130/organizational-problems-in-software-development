# -*- coding: utf-8 -*- 
"""
    Author: 72733
    Datetime: 2024-07-26 15:52
    DESC:
"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def heatmap():
# 你的数据
    data = [
        [0, 0, 0, 7.81, 0, 19.24, 14.43],
        [0, 0, 0, 20.05, 24.05, 15.43, 12.43],
        [0, 0, 0, 7.81, 0, 15.43, 18.24],
        [7.81, 20.05, 7.81, 0, 24.05, 19.24, 4.81],
        [0, 24.05, 0, 24.05, 0, 0, 0],
        [19.24, 15.43, 15.43, 19.24, 0, 0, 0],
        [14.43, 12.43, 18.24, 4.81, 0, 0, 0]
    ]

    # 行列标签E
    row_labels = ['A:Data Scientist Team', 'A:Innovation sector', 'A:IT sector', 'C: CTO', 'B: Customized services sector', 'B:Algorithm sector', 'B:Engineering sector']
    col_labels = ['A:Data Scientist Team', 'A:Innovation sector', 'A:IT sector', 'C: CTO', 'B: Customized services sector', 'B:Algorithm sector', 'B:Engineering sector']

    # 创建DataFrame
    df = pd.DataFrame(data, index=row_labels, columns=col_labels)

    # 绘制热力图
    plt.figure(figsize=(10, 8))  # 设置图形大小
    sns.heatmap(df, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True, xticklabels=df.columns, yticklabels=df.index)

    # 显示图形
    plt.show()

if __name__ == "__main__":
    heatmap()