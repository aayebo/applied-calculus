f <- function(x) x^2
riemann <- function(f, a, b, n, method = "left") {
  h <- (b - a)/n
  i <- 0:(n - 1)
  x <- if (method == "left") a + i*h else
       if (method == "right") a + (i + 1)*h else
       a + (i + 0.5)*h
  h * sum(f(x))
}
for (n in c(4, 8, 16, 64)) {
  cat(n, riemann(f, 0, 2, n, "left"),
      riemann(f, 0, 2, n, "right"),
      riemann(f, 0, 2, n, "midpoint"), "\n")
}
cat("Exact:", 8/3, "\n")
