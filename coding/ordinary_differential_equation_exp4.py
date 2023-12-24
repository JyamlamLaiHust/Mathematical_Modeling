# 常微分方程求数值解 例2

from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import arange
dy = lambda y, x: 1/(1+x**2)-2*y**2
x = arange(0, 10.5, 0.5)
sol = odeint(dy, 0, x)
print("x={}\n对应的数值解y={}".format(x, sol.T))
plt.plot(x, sol)
plt.show()
