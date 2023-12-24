# 常微分方程求符号解 例2
from sympy import *

# 求y
y = symbols('y', cls=Function)
x = symbols('x')
eq = Eq(y(x).diff(x, 2)+4*y(x).diff(x, 1)+29*y(x), 0)
print(dsolve(eq, y(x)))

# 求y的一阶导
C1 = symbols('C1')
C2 = symbols('C2')
f = (C1*sin(5*x) + C2*cos(5*x))*exp(-2*x)
print(f.diff(x, 1))

# 带入等式条件
# (*C1+1*C2)*1=0
# -2*(C1*0+C2*1)*1+(5*C1*1-5*C2*0)*1=15
