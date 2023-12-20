# 线性规划求解

from scipy import optimize
import numpy as np
# 目标函数
c = np.array([2,3,-5])

# 约束条件
A = np.array([[-2,5,-1],[1,3,1]])
b = np.array([-10,12])
Aeq = np.array([[1,1,1]])
beq = np.array([7])

# x1、x2、x3则分别表示三个决策变量的取值范围：None表示无界，即不设置下界或上界；
# (0, None)表示下界为0，上界为无穷大。
x1 = (0,None)
x2 = (0,None)
x3 = (0,None)

# -c表示最大化目标函数，因为linprog函数默认最小化目标函数，所以要将其系数取相反数；
# A和b表示不等式约束条件；
# Aeq和beq表示等式约束条件；
# bounds表示各个决策变量的取值范围。
res = optimize.linprog(-c, A, b, Aeq, beq, bounds=(x1,x2,x3))
print(res)