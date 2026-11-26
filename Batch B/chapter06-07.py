import numpy as np
from scipy.integrate import quad
shell = quad(lambda x: 2*np.pi*x*(4-x*x), 0, 2)[0]
disk = quad(lambda y: np.pi*(4-y), 0, 4)[0]
print(f"Shell: {shell:.6f}")
print(f"Disk:  {disk:.6f}")
print(f"Difference: {abs(shell-disk):.3e}")
print(f"Exact: {8*np.pi:.6f}")
