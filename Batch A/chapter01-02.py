import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(5 - 2*x) / (x + 1)

for left, right in [(-4, -1.02), (-0.98, 2.5)]:
    x = np.linspace(left, right, 400)
    plt.plot(x, f(x))
plt.axvline(-1, linestyle="--", color="gray")
plt.ylim(-12, 12)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
