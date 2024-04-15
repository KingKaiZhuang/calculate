from sympy import *

t = symbols('t', real=True)
h = symbols('h', cls=Function)
k = symbols('k', real=True)  # 定義常數k

# 設置微分方程式
dh_dt = h(t).diff(t, 1)  # dh/dt
rate = sqrt(t)  # 速率
eq = Eq(dh_dt, k * rate)  # dh/dt = k * sqrt(t)

# 解微分方程式
h_sol = dsolve(eq, hint='separable')

# 打印解
pprint(h_sol)
