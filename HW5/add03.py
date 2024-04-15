# (x^3 + y^3)dx + 3xy^2dy = 0
from sympy import *

x, y = symbols('x y')

# 定義微分方程左邊部分 M(x, y) 和 N(x, y)
M = x**3 + y**3
N = 3*x*y**2

# 手動計算偏導數
M_dx = diff(M, x)
N_dy = diff(N, y)

# 打印結果
print("M_dx:", M_dx)
print("N_dy:", N_dy)
