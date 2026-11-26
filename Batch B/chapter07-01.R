f <- function(t) 1/t
for (x in c(0.5, 1, 2, 4)) {
  numerical <- integrate(f, lower=1, upper=x)$value
  cat('x =', x, 'area =', round(numerical, 7),
      'log(x) =', round(log(x), 7), '\n')
}
curve(1/x, from=0.25, to=4, lwd=2,
      xlab='t', ylab='1/t', main='Reciprocal curve')
