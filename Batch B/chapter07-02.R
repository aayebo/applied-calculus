f <- function(t) 12 * 0.8^t
numeric_total <- integrate(f, 0, 5)$value
exact_total <- 12 * (0.8^5 - 1)/log(0.8)
cat('Numerical =', numeric_total, '\n')
cat('Analytical =', exact_total, '\n')
curve(f(x), from=0, to=5, lwd=2,
      xlab='Time (hours)', ylab='Signal per hour')
