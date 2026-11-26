import sympy as sp
x = sp.symbols('x')
f = x**3 - 4*x**2 + 2*x + 1
df = sp.diff(f, x)
print(df)
print(df.subs(x, 2))
