import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2*np.pi, 600)
a = 1
x, y = a*(t-np.sin(t)), a*(1-np.cos(t))
plt.plot(x,y)
idx = np.linspace(0,len(t)-1,15,dtype=int)
plt.scatter(x[idx],y[idx],color="red")
plt.axis("equal"); plt.xlabel("x"); plt.ylabel("y")
plt.title("Cycloid"); plt.show()
