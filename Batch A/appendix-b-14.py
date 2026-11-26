def derivative_centered(fun, a, h=1e-4):
    return (fun(a+h) - fun(a-h)) / (2*h)

def cubic(x):
    return x**3 - 2*x

estimate = derivative_centered(cubic, 2)
exact = 3*2**2 - 2
print(estimate, exact, abs(estimate-exact))
