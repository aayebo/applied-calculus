import numpy as np
def partial_power(x, N):
    n = np.arange(1, N+1)
    return np.sum(((x-2)/3)**n/n)
for x in [-1, 0, 2, 4, 5]:
    print("x =", x, "S100 =", partial_power(x, 100))
