import numpy as np
import matplotlib.pyplot as plt
Q0 = 120
k = np.log(0.6)/4
t = np.linspace(0, 16, 250)
plt.plot(t, Q0*np.exp(k*t))
plt.axhline(Q0/2, linestyle='--')
plt.xlabel('Hours'); plt.ylabel('Amount (mg)')
plt.show()
print('k:', k, 'half-life:', np.log(0.5)/k)
