import numpy as np
import matplotlib.pyplot as plt
T = lambda t: 22 + 60*np.exp(-0.12*t)
t_star = -np.log(0.3)/0.12
print('Threshold time:', t_star)
print('Check:', T(t_star))
t = np.linspace(0, 30, 300)
plt.plot(t, T(t))
plt.axhline(40, linestyle='--')
plt.axhline(22, linestyle=':')
plt.xlabel('Minutes'); plt.ylabel('Temperature (C)')
plt.show()
