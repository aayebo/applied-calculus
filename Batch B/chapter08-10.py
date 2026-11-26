f = lambda x: (5*x+1)/(x*x-x-2)
g = lambda x: (11/3)/(x-2)+(4/3)/(x+1)
xs = [-0.8+2.6*i/200 for i in range(201)]
print('Maximum difference:',max(abs(f(x)-g(x)) for x in xs))
