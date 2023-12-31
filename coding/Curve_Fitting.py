# 拟合方法
# 插值法
import numpy as np
x = np.arange(-1.5, 1.6, 0.5)
y = [-4.45, -0.45, 0.55, 0.05, -0.44, 0.54, 4.55]
an = np.polyfit(x, y, 3)
print(an)
p1 = np.poly1d(an)
print(p1)

# 用statsmodels库
import pandas as pd
import numpy as np
import statsmodels.api as sm  # 实现了类似于二元中的统计模型，比如ols普通最小二乘法
import statsmodels.stats.api as sms  # 实现了统计工具，比如t检验、F检验...
import statsmodels.formula .api as smf
import scipy

np.random.seed(991)  # 随机数种子
x1 = np.random.normal(0, 0.4, 100)  # 生成符合正态分布的随机数(均值,标准差,所生成随机数的个数)
x2 = np.random.normal(0, 0.6, 100)
x3 = np.random.normal(0, 0.2, 100)
eps = np.random.normal(0, 0.05, 100)  # 生成噪声数据，保证后面模拟所生成的因变量的数据比较接近实际的环境
X = np.c_[x1, x2, x3]  # 调用c_函数来生成自变量的数据的矩阵，按照列进行生成的：100x3的矩阵
beta = [0.1, 0.2, 0.7]  # 生成模拟数据时候的系数的值
y = np.dot(X, beta) + eps  # 点积+噪声
X_model = sm.add_constant(X)  # add_constant给矩阵加上一列常量1，主要目的：便于估计多元线性回归模型的截距，也是便于后面进行参数估计时的计算
model = sm.OLS(y, X_model)  # 调用OLS普通最小二乘
results = model.fit()  # fit拟合，主要功能就是进行参数估计，参数估计的主要目的是估计出回归系数。
results.summary()  # summary方法主要是为了显示拟合的结果
print(results.summary())

# 自定义拟合
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
X = np.arange(1, 11, 1)
Y = np.array([1.1, 2.5, 3.6, 4.9, 6.2, 9.0, 9.5, 11.0, 15.6, 14.1])
p = np.polyfit(X, Y,1)
print(p)


def Pfun(x, a, b):
    return 1/(a+b*x)


popt, pcov = curve_fit(Pfun, X, Y)
print(popt)
plt.plot(X, Y, "*", X, np.polyval(p, x), 'r-')
plt.plot(X, Pfun(x, *popt), "b-")
plt.show()