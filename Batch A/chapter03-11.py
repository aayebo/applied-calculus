import numpy as np
import matplotlib.pyplot as plt
T = lambda t: 22+58*np.exp(-0.18*t)
dT = lambda t: -10.44*np.exp(-0.18*t)
print(round(T(5), 3), round(dT(5), 3))
t = np.linspace(0, 30, 301)
plt.plot(t, T(t))
plt.xlabel("time (min)")
plt.ylabel("Temperature (C)")
plt.show()
