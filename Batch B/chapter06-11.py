import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def work(H):
    return quad(lambda y: 1000*9.8*np.pi*(H-y), 0, 3)[0]
heights = np.array([3, 3.5, 4, 5])
values = np.array([work(H) for H in heights])
for H, W in zip(heights, values):
    print(f"Outlet {H:.1f} m: {W:.2f} J")
plt.plot(heights, values, marker="o")
plt.xlabel("Outlet height above bottom (m)")
plt.ylabel("Work (J)")
plt.show()
