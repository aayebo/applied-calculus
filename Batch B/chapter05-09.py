from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
rate = lambda t: 2 + 0.5*t
A = lambda x: quad(rate, 0, x)[0]
x = np.linspace(0, 4, 101)
plt.plot(x, [A(z) for z in x])
plt.xlabel("Time (hours)"); plt.ylabel("Volume (L)")
plt.show()
h = 1e-4
print("Volume:", A(4), "L")
print("Derivative estimate:", (A(2+h)-A(2-h))/(2*h))
print("Rate:", rate(2), "L/hour")
