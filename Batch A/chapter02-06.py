import numpy as np
import matplotlib.pyplot as plt
epsilon = 0.4
delta = min(1, epsilon/5)
x = np.linspace(1.7, 2.3, 400)
plt.plot(x, x**2)
for y in (4-epsilon, 4+epsilon):
    plt.axhline(y, linestyle="--", color="red")
for v in (2-delta, 2+delta):
    plt.axvline(v, linestyle="--", color="blue")
plt.xlabel("x"); plt.ylabel("x^2"); plt.show()
print("epsilon =", epsilon, "delta =", delta)
