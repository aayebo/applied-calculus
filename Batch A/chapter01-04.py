import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 5, 500)
plt.plot(x, x**2, label="x^2")
plt.plot(x, -2*(x-3)**2 + 4, label="-2(x-3)^2+4")
plt.scatter([3], [4])
plt.ylim(-5, 10)
plt.legend()
plt.show()
