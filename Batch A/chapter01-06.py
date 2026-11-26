import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 48, 1000)
T = 18 + 6*np.sin(np.pi*(t - 9)/12)
plt.plot(t, T)
plt.xlabel("Hours")
plt.ylabel("Temperature (C)")
plt.show()
x = np.linspace(0, 1, 1001)
coarse = np.linspace(0, 1, 11)
plt.plot(x, np.sin(20*np.pi*x))
plt.scatter(coarse, np.sin(20*np.pi*coarse), color="red")
plt.show()
