import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
for x in [0.5, 1, 2, 4]:
    numerical = quad(lambda t: 1/t, 1, x)[0]
    print(x, round(numerical, 7), round(np.log(x), 7))
t = np.linspace(0.25, 4, 300)
plt.plot(t, 1/t)
plt.xlabel('t'); plt.ylabel('1/t')
plt.show()
