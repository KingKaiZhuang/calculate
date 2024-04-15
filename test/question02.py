from sympy import symbols, Function, Eq, dsolve, Derivative, integrate, simplify

# 定義變量
x = symbols('x')
y = Function('y')(x)

# 微分方程重新整理後的形式
eq = Eq((2*x**2*y**2 + 1)/(y**4 + 1), -x/y)

# 分離變量並準備積分
lhs = integrate((2*x**2*y**2 + 1)/(y**4 + 1), y)
rhs = integrate(-x/y, x)

# 簡化積分結果（如果可能）
lhs_simplified = simplify(lhs)
rhs_simplified = simplify(rhs)

# 輸出積分結果
print("LHS:", lhs_simplified)
print("RHS:", rhs_simplified)
