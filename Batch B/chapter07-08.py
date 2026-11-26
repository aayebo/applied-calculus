import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
f = lambda t: 12 * 0.8**t
numerical = quad(f, 0, 5)[0]
exact = 12 * (0.8**5 - 1)/np.log(0.8)
print('Numerical:', numerical, 'Analytical:', exact)
t = np.linspace(0, 5, 200)
plt.plot(t, f(t))
plt.xlabel('Time (hours)'); plt.ylabel('Signal per hour')
plt.show()
