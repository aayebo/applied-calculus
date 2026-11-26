import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
area = lambda x: np.sqrt(3)/4*(2-x)**2
volume = quad(area, 0, 2)[0]
print("Volume:", volume)
x = np.linspace(0, 2, 200)
plt.plot(x, area(x))
plt.xlabel("Position x")
plt.ylabel("Cross-sectional area A(x)")
plt.show()
