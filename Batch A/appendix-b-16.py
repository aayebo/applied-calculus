def midpoint_rule(fun, a, b, n):
    width = (b-a)/n
    midpoints = a + (np.arange(n)+0.5)*width
    return width*np.sum(fun(midpoints))

for n in [4, 10, 50, 200]:
    print(n, midpoint_rule(lambda x: x**2, 0, 2, n))
print("Exact:", 8/3)
