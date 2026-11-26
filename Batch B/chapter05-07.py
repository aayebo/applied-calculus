def riemann(f, a, b, n, method="left"):
    h = (b-a)/n
    offsets = {"left": 0, "right": 1, "midpoint": 0.5}
    shift = offsets[method]
    return h * sum(f(a+(i+shift)*h) for i in range(n))

f = lambda x: x*x
for n in (4, 8, 16, 64):
    print(n, *(round(riemann(f, 0, 2, n, method), 8)
               for method in ("left", "right", "midpoint")))
print("Exact:", 8/3)
