# dy/dx = -2xy^3-4 / 3x^2y^2 + e^y 
from sympy import *

x, y = symbols('x y')
y_func = Function('y')

# 定義微分方程式
f = -2*x*y**3 - 4/(3*x**2*y**2) + exp(y)
eq = Eq(y_func(x).diff(x), f)

# 解微分方程式
y_sol = dsolve(eq)

# 打印解
pprint(y_sol)
