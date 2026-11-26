import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
a = 3
x = np.linspace(-4, 4, 250)
plt.plot(x, a*np.cosh(x/a))
plt.xlabel('x'); plt.ylabel('Cable height')
plt.show()
length_num = quad(lambda x: np.cosh(x/a), -3, 3)[0]
length_exact = 6*np.sinh(1)
print('Numerical:', length_num, 'Exact:', length_exact)
