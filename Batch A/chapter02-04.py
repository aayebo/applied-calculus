import numpy as np
import matplotlib.pyplot as plt
for lo, hi in [(-1, 0.95), (1.05, 3)]:
    x = np.linspace(lo, hi, 400)
    plt.plot(x, 1/(x - 1))
plt.axvline(1, linestyle="--", color="gray")
plt.xlim(-1, 3); plt.ylim(-15, 15)
plt.xlabel("x"); plt.ylabel("f(x)"); plt.show()
