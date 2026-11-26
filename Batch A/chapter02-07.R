f <- function(x) x^3 - x - 1
a <- 1; b <- 2; tolerance <- 1e-6
while ((b-a)/2 > tolerance) {
  m <- (a+b)/2
  if (f(a)*f(m) <= 0) b <- m else a <- m
}
root <- (a+b)/2
cat("Root estimate:", format(root, digits = 12), "\n")
cat("Guaranteed error <=", (b-a)/2, "\n")
stopifnot(abs(f(root)) < 1e-4)
