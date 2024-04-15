from sympy import *

# 定義符號
t = symbols('t')
y = symbols('y', cls=Function)
eq = Eq(0.08*t+2*y(t)*y(t).diff(t,1), 0)
ysol = dsolve(eq, ics={y(0): 10})
pprint(ysol)
vy = ysol.rhs.diff(t)
print("y的速率為:", end='')
pprint(vy)
fvy = lambdify(t, vy)
print(f't=30時y的速率為{fvy(30)}m/s')