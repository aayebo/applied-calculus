import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 2, 401)
t3 = x - x**3/6
t5 = t3 + x**5/120
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, t3, "--", label="Degree 3")
plt.plot(x, t5, ":", label="Degree 5")
plt.legend()
plt.show()
print(abs(np.sin(0.5) - (0.5-0.5**3/6+0.5**5/120)))
