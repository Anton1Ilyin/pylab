import sympy
import numpy as np
from scipy.integrate import odeint
x=sympy.symbols('x')
y=sympy.symbols('y',cls=sympy.Function)
diff=sympy.Eq(y(x).diff(x),-2*y(x)+sympy.sqrt(2))
s=sympy.dsolve(diff, y(x))
C1=sympy.symbols('C1')
print('Sympy:')
print(s)
print(sympy.solve(s.subs({x: 0, y: sympy.sqrt(2)}),C1))
print('Scipy:')
def pend(y,t):
    d0, d1=y
    dydt=[d1, -2*d0-np.sqrt(2)]
    return dydt
y0=[np.sqrt(2),-np.sqrt(2)]
#t=np.array([0])
t=np.linspace(0,10,10)
sol=odeint(pend, y0, t)
print(t)
print(sol[:,0])


