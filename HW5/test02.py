from sympy import *

x = symbols('x', real=True)
y = symbols('y', cls=Function)
eq = Eq(y(x).diff(x, 1)-0.05*y(x),0)
ysol = dsolve(eq, ics={y(0):1})
pprint(ysol)
n = symbols('n')
eql = exp(0.05*n)-2
nsol_txt = solve(eql)
nsol_num = nsolve(eql, n, 1)
print(f'symbol sol = {nsol_txt}')
print(f'numberical sol = {nsol_num}')