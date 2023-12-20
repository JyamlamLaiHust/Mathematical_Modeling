# 求解三元一次方程组

# Method 1-克莱姆法则（两边同时乘A的逆矩阵）
import numpy as np
A = np.array([[10, -1, -2], [-1, 10, -2],[-1,-1, 5]])# A为系数矩阵
b = np.array([72, 83, 42])# b为常数列
inv_A = np.linalg.inv(A)# A的逆矩阵
x = inv_A.dot(b)# A的逆矩阵与b做点积运算
print(x)
x = np.linalg.solve(A, b)# 7,8两行也可以用本行替代print(x)
print(x)

# Method 2-直接用函数求解
from sympy import symbols, Eq, solve
x, y, z = symbols('x y z')
eqs = [Eq(10 * x - y - 2 * z,72),
       Eq(-x + 10 * y - 2 * z, 83),
       Eq(-x - y + 5 * z, 42)]
print(solve(eqs,[x,y,z]))