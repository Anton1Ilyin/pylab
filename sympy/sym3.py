import sympy
from scipy.integrate import odeint
x=sympy.symbols('x')
y=sympy.symbols('y',cls=sympy.Function)
diff=sympy.Eq(y(x).diff(x),-2*y(x)+sympy.sqrt(2))
s=sympy.dsolve(diff, y(x))
C1=sympy.symbols('C1')
print(sympy.solve(s.subs({x: 0, y: sympy.sqrt(2)}),C1))