from sympy import *

# 定義符號
k, x = symbols('k x', real=True)
y = symbols('y', cls=Function)
eq = Eq(y(x).diff(x, 1),k*y(x))
ysol = dsolve(eq, ics={y(0):1})
pprint(ysol)
ksol = solve(exp(k*50)-2)
for i in range(len(ksol)):
    print(f'i={i}, sol={ksol[i]}')

k1 = ksol[0]
n = symbols('n')
nsol = nsolve(exp(k1*n)-3,n,51)
print(f'nsol={nsol}')
