from sympy import *

# 定義符號
x = symbols('x', real=True)
y = symbols('y', cls=Function)
eq = Eq(y(x).diff(x,1),(1+y(x)**2)/(2+3*x))
ysol = dsolve(eq, hint='separable')
pprint(ysol)