import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0,2*np.pi,1200)
fig,ax = plt.subplots(1,2,figsize=(10,4))
for a,r,title in [(ax[0],2*(1+np.cos(theta)),"Cardioid"),
                  (ax[1],3*np.cos(2*theta),"Four-petal rose")]:
    a.plot(r*np.cos(theta),r*np.sin(theta))
    a.set_aspect("equal"); a.set_title(title)
plt.show()
