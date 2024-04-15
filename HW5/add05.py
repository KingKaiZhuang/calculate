from sympy import *

x, y = symbols('x y')
y_func = Function('y')

# 定義微分方程式
f = exp(y) / (1 - x*exp(y))
eq = Eq(y_func(x).diff(x), f)

# 解微分方程式
y_sol = dsolve(eq)

# 打印解
pprint(y_sol)
