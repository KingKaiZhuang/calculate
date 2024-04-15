from sympy import *
k, t = symbols('k t', real=True)
P = symbols('P', cls=Function)
eq = Eq(P(t).diff(t,1),k*(P(t)-P(t)**3))
Psol = dsolve(eq, hint='separable')
P2 = (Psol[1].rhs)**2
pprint(latex(Psol))
pprint(latex(P2))