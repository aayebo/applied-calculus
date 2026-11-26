from scipy.integrate import quad
f = lambda x: 4-x*x
A = quad(f, -2, 2)[0]
My = quad(lambda x: x*f(x), -2, 2)[0]
Mx = quad(lambda x: 0.5*f(x)**2, -2, 2)[0]
print("Area:", A)
print("Centroid x:", My/A)
print("Centroid y:", Mx/A)
