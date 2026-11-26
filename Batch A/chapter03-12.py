import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(12, 20, 201)
f = np.sqrt(x)
L = 4 + (x-16)/8
plt.plot(x, f, label="sqrt(x)")
plt.plot(x, L, "--", label="linearization")
plt.legend(); plt.show()
print(abs(np.sqrt(16.4)-4.05))
