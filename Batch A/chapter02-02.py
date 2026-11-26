import numpy as np
import matplotlib.pyplot as plt
h = 10.0**(-np.arange(1, 15))
naive = (np.sqrt(9 + h) - 3) / h
stable = 1 / (np.sqrt(9 + h) + 3)
for hi, ni, si in zip(h, naive, stable):
    print(f"h={hi:.1e}, naive={ni:.9f}, stable={si:.9f}")
plt.loglog(h, np.abs(naive - 1/6), "o", label="naive")
plt.loglog(h, np.abs(stable - 1/6), "s", label="stable")
plt.xlabel("h"); plt.ylabel("Absolute error")
plt.legend(); plt.show()
