import numpy as np
f = lambda x: x**2 + 2*x
a = 3
for h in 10.0**(-np.arange(1, 7)):
    secant = (f(a+h)-f(a))/h
    print(h, secant, abs(secant-8))
