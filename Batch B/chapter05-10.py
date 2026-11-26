import math
from scipy.integrate import quad
f = lambda x: math.exp(-x*x)
for n in (10, 20, 40, 80):
    h = 2/n
    midpoint = h*sum(f((i+0.5)*h) for i in range(n))
    print("n =", n, "midpoint =", midpoint)
print("Adaptive quadrature:", quad(f, 0, 2)[0])
