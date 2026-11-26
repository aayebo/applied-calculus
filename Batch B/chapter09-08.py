import numpy as np
import matplotlib.pyplot as plt
n = np.arange(1, 301)
geo = np.cumsum(0.7**(n - 1))
harmonic = np.cumsum(1/n)
plt.plot(n, harmonic, label="Harmonic")
plt.plot(n, geo, "--", label="Geometric")
plt.xlabel("Number of terms")
plt.ylabel("Partial sum")
plt.legend()
plt.show()
print("Geometric limit:", 1/(1-0.7))
