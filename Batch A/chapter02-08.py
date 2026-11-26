def f(x):
    return x**3 - x - 1

a, b, tolerance = 1.0, 2.0, 1e-6
while (b-a)/2 > tolerance:
    m = (a+b)/2
    if f(a)*f(m) <= 0:
        b = m
    else:
        a = m
root = (a+b)/2
print("Root estimate:", root)
print("Guaranteed error <=", (b-a)/2)
assert abs(f(root)) < 1e-4
