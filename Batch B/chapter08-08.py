from math import sin, cos
F = lambda x: -cos(x)**3/3+cos(x)**5/5
f = lambda x: sin(x)**3*cos(x)**2
h = 1e-5
xs = [-2+4*i/100 for i in range(101)]
errors = [abs((F(x+h)-F(x-h))/(2*h)-f(x)) for x in xs]
print('Maximum discrepancy:',max(errors))
