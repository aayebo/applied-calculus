import numpy as np
import matplotlib.pyplot as plt
f = lambda x: x**3 - 3*x + 1
fp = lambda x: 3*x**2 - 3
x = np.linspace(-2,2,401)
plt.plot(x,f(x),label="f(x)")
candidates = np.array([-2,-1,1,2])
plt.scatter(candidates,f(candidates),color="red")
plt.xlabel("x"); plt.ylabel("f(x)"); plt.legend(); plt.show()
for c in candidates:
    print(f"x={c:.0f}, f(x)={f(c):.0f}, f'(x)={fp(c):.0f}")
