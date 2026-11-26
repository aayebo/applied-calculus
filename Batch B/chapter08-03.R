f <- function(x) sqrt(9-x^2)
F <- function(x) x*sqrt(9-x^2)/2 + 9*asin(x/3)/2
numeric <- integrate(f, lower=-2, upper=2)$value
exact <- F(2)-F(-2)
cat('Quadrature:', numeric, ' analytical:', exact, '\n')
curve(f(x), from=-3, to=3, lwd=2,
      xlab='x', ylab='Cross-sectional height')
