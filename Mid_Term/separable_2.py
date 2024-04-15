# 解正合型 (2x3+3y)dx + (3x+y-1)dy = 0
from sympy import *

x = symbols('x')
y = symbols('y', cls=Function)

eq = Eq((2*x**3 + 3*y(x) + (3*x+y(x)-1)*y(x).diff(x,1)),0)

ysol = dsolve(eq, hint='1st_exact')

pprint(ysol)
ylatex = latex(ysol)
pprint(ylatex)