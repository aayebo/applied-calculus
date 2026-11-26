import sympy as sp
x = sp.symbols('x', positive=True)
S = 2*sp.pi*x**2 + 2*1000/x
print('Derivative:',sp.diff(S,x))
print('Second derivative:',sp.diff(S,x,2))
print('Stationary radius:',sp.solve(sp.diff(S,x),x))
