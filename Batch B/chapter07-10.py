import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 20, 300)
y = 50/(1 + 4*np.exp(-0.4*t))
plt.plot(t, y)
plt.axhline(50, linestyle='--')
plt.xlabel('Time'); plt.ylabel('Population')
plt.show()
print('At t=10:', 50/(1 + 4*np.exp(-4)))
