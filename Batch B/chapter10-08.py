import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,2*np.pi,400)
x,y = 3*np.cos(t),2*np.sin(t)
t0 = np.pi/3
slope = -2*np.cos(t0)/(3*np.sin(t0))
x0,y0 = 3*np.cos(t0),2*np.sin(t0)
xx = np.linspace(x0-.8,x0+.8,100)
plt.plot(x,y); plt.plot(xx,y0+slope*(xx-x0),color="red")
plt.axis("equal"); plt.show()
print("Tangent slope:",slope)
