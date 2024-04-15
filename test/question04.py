from sympy import *

t = symbols('t')
P = Function('P')(t)
r = 0.06  # 年利率

# 建立微分方程
eq = Eq(P.diff(t), r*P)

# 解微分方程
solution = dsolve(eq, P)

# 使用初始條件求解常數C1
C1_eq = solution.subs(t, 0).subs(P, 100000)
C1 = solve(C1_eq)

# 將C1值代回解中
final_solution = solution.subs('C1', C1[0])

# 求解當P(t) = 250000時的t值
target_eq = Eq(final_solution.rhs, 250000)
t_value = solve(target_eq, t)

# 以 LaTeX 格式輸出解
print(f'LaTeX 表達式: {latex(final_solution)}')


