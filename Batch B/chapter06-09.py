import numpy as np
from scipy.integrate import quad
def polygon_length(n):
    x = np.linspace(0, 1, n+1)
    y = x**2
    return np.sum(np.hypot(np.diff(x), np.diff(y)))
reference = quad(lambda x: np.sqrt(1+4*x*x), 0, 1)[0]
for n in [4, 8, 16, 32, 64, 128]:
    estimate = polygon_length(n)
    print(f"n={n:3d}, length={estimate:.8f}, error={reference-estimate:.8f}")
