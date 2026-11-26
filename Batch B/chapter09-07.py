import numpy as np
import matplotlib.pyplot as plt
n = np.arange(1, 101)
terms = (-1.0)**(n - 1) / n
partial = np.cumsum(terms)
plt.scatter(n, partial, s=10)
plt.axhline(np.log(2), linestyle="--")
plt.xlabel("Number of terms")
plt.ylabel("Partial sum")
plt.show()
print("100-term estimate:", partial[-1])
print("Exact limit:", np.log(2))
