# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pandas as pd
import numpy as np

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def singularCompution():
    # 定义组织结构图的邻接矩阵
    # 1: A-CDO, 2: A-Technical Manager,
    # 3: A-Innovation Manager, 4: A-Operation1,
    # 5: A-Operation2, 6: A-ProjectManager,
    # 7: A-IT manager, 8: A-IT Development,
    # 9: C-CTO, 10: C-Domain Expert,
    # 11: C-Data Team, 12: B-Project Manager,
    # 13: B-algorithm engineer, 14: B-AI Architect,
    # 15: B-pre - sales, 16: B-Engineering Manager,
    # 17: B-Product Manager, 18: B-frontend development,
    # 19: B-backend development, 20: B-Test Deployment

    edges = [(2, 9), (2, 14), (2, 15), (6, 9), (6, 12), (6, 14), (6, 15),
             (7, 9), (7, 14), (7, 15), (9, 12), (9, 14), (9, 15)]

    # 创建一个20x20的DataFrame，索引和列名从1开始，实际索引从0开始
    df = pd.DataFrame(index=range(20), columns=range(20))
    df = df.fillna(0)

    # 填充邻接矩阵
    for edge in edges:
        u, v = edge  # 节点编号从1开始，需要减1以匹配Pandas的索引
        df.at[u - 1, v - 1] = 1
        df.at[v - 1, u - 1] = 1  # 因为是无向图，所以需要填充两个方向

    # 转换为NumPy数组，并确保数据类型为float64
    adjacency_matrix = df.to_numpy(dtype='float64')

    # print("邻接矩阵：")
    # print(adjacency_matrix)

    # 计算奇异值分解
    s, u, vh = np.linalg.svd(adjacency_matrix)
    print("奇异值：", s)

    sum_of_singular = np.sum(s)

    return sum_of_singular

def communicationCompution():
    edges = [(2, 9, 4), (2, 14, 4), (2, 15, 3), (6, 9, 1), (6, 12, 5), (6, 14, 4), (6, 15, 1),
             (7, 9, 4), (7, 14, 4), (7, 15, 3), (9, 12, 5), (9, 14, 4), (9, 15, 1)]

    # 创建一个20x20的DataFrame，索引和列名从1开始，实际索引从0开始
    df = pd.DataFrame(index=range(20), columns=range(20))
    df = df.fillna(0)

    # 填充邻接矩阵
    for edge in edges:
        u, v, k = edge  # 节点编号从1开始，需要减1以匹配Pandas的索引
        df.at[u - 1, v - 1] = 1*k
        df.at[v - 1, u - 1] = 1*k  # 因为是无向图，所以需要填充两个方向

    # 转换为NumPy数组，并确保数据类型为float64
    adjacency_matrix = df.to_numpy(dtype='float64')

    print("通信复杂度邻接矩阵：")
    print(adjacency_matrix)

    sum_of_txcomplexity = np.sum(adjacency_matrix)/2

    return sum_of_txcomplexity, adjacency_matrix

def factorCompution():
    edges = [(2, 9, 1), (2, 14, 4), (2, 15, 3), (6, 9, 5), (6, 12, 5), (6, 14, 3), (6, 15, 3),
             (7, 9, 1), (7, 14, 3), (7, 15, 4), (9, 12, 5), (9, 14, 4), (9, 15, 1)]

    # 创建一个20x20的DataFrame，索引和列名从1开始，实际索引从0开始
    df = pd.DataFrame(index=range(20), columns=range(20))
    df = df.fillna(0)

    import numpy as np

    # 初始化权重向量及复杂度向量
    vector1 = np.array([0.2, 0.1, 0.15, 0.3, 0.1, 0.02, 0.1, 0.01, 0.02])
    vector2 = np.array([3, 3, 4, 5, 3, 3, 4, 3, 1])

    # 计算点积
    f = np.dot(vector1, vector2)

    # 打印结果
    print("向量1:", vector1)
    print("向量2:", vector2)
    print("向量1和向量2的点积:", f)

    # 填充邻接矩阵
    for edge in edges:
        u, v, k = edge  # 节点编号从1开始，需要减1以匹配Pandas的索引
        df.at[u - 1, v - 1] = 1*k*f
        df.at[v - 1, u - 1] = 1*k*f  # 因为是无向图，所以需要填充两个方向

    # 转换为NumPy数组，并确保数据类型为float64
    adjacency_matrix = df.to_numpy(dtype='float64')

    print("因素复杂度邻接矩阵：")
    print(adjacency_matrix)

    sum_of_jkcomplexity = np.sum(adjacency_matrix)/2

    return sum_of_jkcomplexity, adjacency_matrix

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    sum1 = singularCompution()
    sum2, matrix1 = communicationCompution()
    sum3, matrix2 = factorCompution()
    sum = (sum1+sum2+sum3)
    sum_matrix = matrix1 + matrix2
    print("总复杂度：",sum)
    print("每对之间复杂度矩阵：", sum_matrix)
