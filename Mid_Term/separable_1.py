# y' - 2x/y = 0
from sympy import *

x = symbols('x')
y = symbols('y', cls=Function)

eq = Eq(y(x).diff(x) - 2*x/y(x), 0)

ysol = dsolve(eq)
pprint(ysol)

ylatex = latex(ysol)
pprint(ylatex)