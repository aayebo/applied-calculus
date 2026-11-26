import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(-2.2,2.2,1000)
fig,ax = plt.subplots(1,3,figsize=(12,4))
for a,e in zip(ax,[.5,1,1.4]):
    den = 1+e*np.cos(theta)
    r = np.where(den>.08,3/den,np.nan)
    a.plot(r*np.cos(theta),r*np.sin(theta))
    a.set_aspect("equal"); a.set_title(f"e = {e}")
plt.show()
