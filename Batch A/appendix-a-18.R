f <- function(x) exp(-x^2)
result <- integrate(f, lower = 0, upper = 1)
result$value
result$abs.error
