import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
alpha = (-1+math.sqrt(17))/2
top = lambda x: 4-x*x
bottom = lambda x: x
area = quad(lambda x: top(x)-bottom(x), 0, alpha)[0]
print("Intersection:", alpha, "Area:", area)
x = np.linspace(0, alpha, 200)
plt.plot(x, top(x)); plt.plot(x, bottom(x), linestyle="--")
plt.fill_between(x, bottom(x), top(x), alpha=0.2)
plt.xlabel("x"); plt.ylabel("y"); plt.show()
