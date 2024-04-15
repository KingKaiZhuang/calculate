from sympy import *

k,p = symbols('k p', real=True)
v = symbols('v', cls=Function)
eg = Eq(v(p).diff(p,1), k * (-v(p)/(p**2)))
Vsol = dsolve(eg, hint='separable')
pprint(Vsol)