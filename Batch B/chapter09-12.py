import math
import numpy as np
n = np.arange(0, 9)
terms = np.array([(-1)**int(k)*0.5**(2*int(k)+1)/
                  (math.factorial(int(k))*(2*int(k)+1))
                  for k in n])
approx = np.cumsum(terms)
x = np.linspace(0, 0.5, 100001)
reference = np.trapezoid(np.exp(-x*x), x)
for k, estimate in zip(n, approx):
    print(k, estimate, abs(estimate-reference))
