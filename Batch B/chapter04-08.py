import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5,3.5,300)
secant_slope = (3**2-1**2)/(3-1)
c = secant_slope/2
plt.plot(x,x*x,label="f(x)=x^2")
plt.plot(x,4*x-3,label="secant")
plt.plot(x,4*x-4,"--",label="parallel tangent")
plt.legend(); plt.show()
print("MVT point:",c)
