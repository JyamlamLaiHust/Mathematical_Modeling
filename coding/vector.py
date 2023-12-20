# python向量运算
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
c = np.array([[1,2,3]])
d = np.array([[9,8,7],[3,2,1]])
# 矩阵加法
sum = a + d
print(sum)
# 放缩
e = 3 * a
print(e)
#数乘、矩阵乘
e = np.dot(a,b)
print(e)
#元素乘
e = a * d
print(e)
#转置
e = c.T
print(e)
e = np.array([[1,2],[3,4]])
#逆矩阵
result = np.linalg.inv(e)
print(result)
#行列式
result = np.linalg.det(e)
print(result)
# 矩阵的秩
e = np.linalg.matrix_rank(d)
print(e)