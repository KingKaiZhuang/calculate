#  y' = 3x^2(y+2),y(1) = 8
from sympy import *

x = symbols('x')
y = symbols('y', cls=Function)

# 設置微分方程式
eq = Eq(y(x).diff(x), 3*x**2*(y(x) + 2))  # y' = 3x^2(y + 2)

# 解微分方程式並加入初始條件
y_sol = dsolve(eq, y(x), ics={y(1): 8})

# 打印解
pprint(y_sol)
