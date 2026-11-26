import numpy as np
import matplotlib.pyplot as plt
x_star = (25-5*np.sqrt(7))/3
V = lambda x: x*(30-2*x)*(20-2*x)
x = np.linspace(0,10,300)
plt.plot(x,V(x)); plt.axvline(x_star,color="red",linestyle="--")
plt.xlabel("Cut size (cm)"); plt.ylabel("Volume (cm^3)")
plt.show()
print("Optimal cut:",x_star,"Maximum volume:",V(x_star))
