from sympy import *

t = symbols('t', real=True)
x = symbols('x', cls=Function)
eq = Eq(x(t).diff(t,1)-x(t)-2,0)
xsol = dsolve(eq, ics={x(t).diff(t,1).subs(t,0):5})
pprint(xsol)