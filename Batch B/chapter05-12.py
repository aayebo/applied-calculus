import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
C = lambda t: 3 + 12*math.exp(-0.4*t)
auc = quad(C, 0, 8)[0]
print("AUC:", auc, "mg*h/L")
print("Mean concentration:", auc/8, "mg/L")
t = np.linspace(0, 8, 200)
plt.plot(t, [C(z) for z in t])
plt.xlabel("Time (h)"); plt.ylabel("Concentration (mg/L)")
plt.show()
