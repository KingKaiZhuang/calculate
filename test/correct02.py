from sympy import *

# 定義符號
x = symbols('x', real=True)
y = symbols('y', cls=Function)
eq = Eq(y(x).diff(x,1)*y(x)*(2*(x**2)*(y(y(x)**2)+1))+x*(1+y(x)**4),0)
ysol = dsolve(eq, hint='1st_exact')
pprint(ysol)