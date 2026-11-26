def f_lab(x):
    return x**3 - 3*x + 1

a = 2
slope = derivative_centered(f_lab, a)
x = np.linspace(1.5, 2.5, 250)
line = f_lab(a) + slope*(x-a)
plt.plot(x, f_lab(x), label="f(x)")
plt.plot(x, line, "--", label="Tangent")
plt.scatter([a], [f_lab(a)])
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
print("Numerical slope:", slope)
