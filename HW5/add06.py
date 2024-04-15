from sympy import *

x, y = symbols('x y')
y_func = Function('y')

# 定義微分方程的左側 M(x, y) 和 N(x, y)
M = x - y**2
N = 2*x*y

# 確認微分方程是否是恰當微分方程
M_dy = diff(M, y)
N_dx = diff(N, x)
is_exact = simplify(M_dy - N_dx) == 0

if is_exact:
    # 設置恰當微分方程式
    eq = Eq(M, N)

    # 解恰當微分方程式
    y_sol = dsolve(eq)

    # 打印解
    pprint(y_sol)
else:
    print("微分方程不是恰當微分方程")
