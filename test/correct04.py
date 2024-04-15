from sympy import *

# 定義符號
t = symbols('t')
y = symbols('y', cls=Function)
eq = Eq(y(t).diff(t,1),0.06*y(t))
ysol = dsolve(eq, ics={y(0): 10})
pprint(ysol)
y_num = ysol.rhs
eq_num = y_num -25
y_num_sol = solve(eq_num, t)
print(y_num_sol[0])