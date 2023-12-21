# 指派问题 整数规划法例题
from scipy.optimize import linear_sum_assignment
import numpy as np
cost = np.array([[25, 29, 31, 42], [39, 38, 26, 20], [34, 27, 28, 40], [24, 42, 36, 23]])
row_ind, col_ind = linear_sum_assignment(cost)
print(row_ind)  # 开销矩阵对应的行索引
print(col_ind)  # 对应行索引的最优指派的列索引
print(cost[row_ind, col_ind])  # 提取每个行索引的最优指派列索引所在的元素，形成数组
print(cost[row_ind, col_ind].sum())  # 数组求和
