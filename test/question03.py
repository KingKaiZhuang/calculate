from sympy import symbols, Function, dsolve, Eq, exp, latex

x = symbols('x')
y = Function('y')(x)

# 定義微分方程
eq = Eq(y.diff(x) + (3/x)*y, exp(x)/x**3)

# 求解微分方程
solution = dsolve(eq, y)

# 以LaTeX格式輸出解
latex_solution = latex(solution)
print(latex_solution)
