import numpy as np
N = np.array([5, 10, 20, 50, 100])
for n in N:
    print(n, 1/(2*(n+1)**2), 1/(2*n**2))
print("Smallest N:", next(n for n in range(1, 101)
                          if 1/(2*n*n) < 0.001))
