from math import sqrt, asin
f = lambda x: sqrt(9-x*x)
F = lambda x: x*sqrt(9-x*x)/2+9*asin(x/3)/2
n = 10000
a,b = -2.0,2.0
h = (b-a)/n
midpoint = h*sum(f(a+(i+0.5)*h) for i in range(n))
print('Midpoint:',midpoint,'Analytical:',F(b)-F(a))
