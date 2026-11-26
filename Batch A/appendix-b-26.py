def rate(t):
    return 4 + 0.5*t

for n in [4, 12, 48, 192]:
    print(n, midpoint_rule(rate, 0, 12, n))
value, err = integrate.quad(rate, 0, 12)
print("Numerical integral:", value)
print("Exact integral:", 84)
