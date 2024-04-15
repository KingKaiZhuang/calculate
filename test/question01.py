from sympy import symbols, Function, Eq, dsolve, latex

# 定義符號和函數
x = symbols('x')
y = Function('y')(x)

# 定義微分方程
eq = Eq(y.diff(x) - (1 + y**2) / (2 + 3*x), 0)

# 使用dsolve求解
ysol = dsolve(eq, y)

# 以LaTeX格式輸出解
latex_solution = latex(ysol)
print(latex_solution)
