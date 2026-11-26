from math import exp
F = lambda x: exp(2*x)*(x*x/2-x/2+1/4)
f = lambda x: x*x*exp(2*x)
h = 1e-5
for x in [0, 0.5, 1, 2]:
    d = (F(x+h)-F(x-h))/(2*h)
    print(x, round(d,6), round(f(x),6))
