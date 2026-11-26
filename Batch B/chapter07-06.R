a <- 3
x <- seq(-4, 4, length.out=250)
y <- a*cosh(x/a)
plot(x, y, type='l', lwd=2,
     xlab='x', ylab='Cable height')
length_num <- integrate(function(x) cosh(x/a), -3, 3)$value
length_exact <- 6*sinh(1)
cat('Numerical length:', length_num, '\n')
cat('Exact length:', length_exact, '\n')
