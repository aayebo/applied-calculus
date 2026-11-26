from scipy.integrate import quad
value, error_estimate = quad(lambda x: x**2, 0, 2)
print(value, error_estimate)
