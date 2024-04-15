from sympy import *

k, x = symbols('k x', real=True)
y = symbols('y', cls=Function)
eq = Eq(y(x).diff(x, 1), k*y(x))
ysol = dsolve(eq)