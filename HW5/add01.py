# y' + x / y =0
from sympy import *

x, y = symbols('x y')
y_func = Function('y')

# 設置微分方程式
eq = Eq(y_func(x).diff(x), -x/y_func(x))  # y' = -x/y

# 解微分方程式
y_sol = dsolve(eq, y_func(x))

# 打印解
pprint(y_sol)
