# 非线性规划模型 求解二次规划例题

from scipy.optimize import minimize
import numpy as np


# 目标函数即min(FG1+FG2+FG3)
def fun(x):
    return (4+0.3*x[0]+0.0007*x[0]*x[0] + 3+0.32*x[1]+0.0004*x[1]*x[1] + 3.5+0.3*x[2]+0.00045*x[2]*x[2])


def con():
    # 约束条件分为eq和ineq
    # eq表示函教结果等于0 ;ineq表示表达式大于等于0
    cons = ({'type': 'eq', 'fun': lambda x: x[0]+x[1]+x[2]-700})
    # {'type':"ineq',"fun': lambda x: -x[2] + x2max} # 如果有不等式约束
    # cons= ([con1，con2，con3，con4，con5，con6，con7，con8]) # 如果有多个约束，则最后返回结果是这个
    # x[0] 其中的0 必须是具体数，不能是t 等参数
    return cons


# 上下限约束
b1 = (100, 200)  #
b2 = (120, 250)  #
b3 = (150, 300)  #
bnds = (b1, b2, b3)  # 边界约束
if __name__ == "__main__":
    cons = con()  # 约束
    # 设置x初始猜测值
    x0 = np.array((150, 250, 20))
    # 光标选中method会显示出不同的方法，不同方法会得出不同的结果，并不是每一种方法计算出的结果都适合当前应用题
    res = minimize(fun, x0, method='SLSQP', constraints=cons, bounds=bnds)
    print("代价", res.fun)
    print(res.success)
    print('解', res.x)


# 遗传算法求解约束极值函数
def object_func(x):
    return (4+0.3*x[0]+0.0007*x[0]*x[0] + 3+0.32*x[1]+0.004*x[1]*x[1] + 3.5+0.3*x[2]+0.00045*x[2]*x[2])


# 等式约束
def cons1(x):
    return [x[0]+x[1]+x[2]-700]


cons = cons1
# 导入包
from sko.GA import GA
# GA(算法对象, 自变量个数, 候选解个数(可变), 下界, 上界, 等式约束条件)
ga = GA(func=object_func, n_dim=3, size_pop=500, max_iter=800, lb=[100, 120, 150], ub=[200, 250, 300], constraint_eq=[cons])
best_x, best_y = ga.run()
print("best_x", best_x, '\n', "best_y", best_y)