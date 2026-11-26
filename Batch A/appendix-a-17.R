midpoint_sum <- function(f, a, b, n = 100) {
  dx <- (b - a) / n
  midpoints <- a + ((1:n) - 0.5) * dx
  sum(f(midpoints)) * dx
}
f <- function(x) x^2
midpoint_sum(f, 0, 2, n = 10)
midpoint_sum(f, 0, 2, n = 1000)
8/3                         # Exact integral
