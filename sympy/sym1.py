from sympy import symbols, Eq, solve,Matrix
import numpy as np
mu,lamda,ro=symbols('mu lambda ro')
m=(-1/ro)*np.eye(9,k=3)
m[3:,:]=np.zeros_like(m[3:,:])
n=(-mu)*np.eye(9, k=-3)
n[:3,:],n[6:,:]=np.zeros_like(n[:3,:]),np.zeros_like(n[6:,:])
m+=n
m[3,0],m[8,0],m[6,0]=-(lamda+2*mu),-lamda,-lamda
print(m)
print("-------------")
x = symbols('x')
m-=x*np.eye(9)
m=Matrix(m)
f=m.det()
e=Eq(f,0)
result = solve(e,x)
for i, root in enumerate(result):
    print(f'Root {i}: {root}')