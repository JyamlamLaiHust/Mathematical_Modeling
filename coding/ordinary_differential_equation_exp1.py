# 求解常微分方程求符号解 例题1
from sympy import *
y = symbols('y', cls=Function)
x = symbols('x')
eq = Eq(y(x).diff(x, 2)+2*y(x).diff(x, 1)+y(x), x*x)
print(dsolve(eq, y(x)))

