from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
v = lambda t: t - 2
print("Displacement:", quad(v, 0, 4)[0], "m")
print("Distance:", quad(lambda t: abs(v(t)), 0, 4)[0], "m")
t = np.linspace(0, 4, 301)
plt.plot(t, v(t)); plt.axhline(0, linestyle="--")
plt.xlabel("Time (s)"); plt.ylabel("Velocity (m/s)")
plt.show()
