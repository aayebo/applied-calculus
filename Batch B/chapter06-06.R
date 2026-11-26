f <- function(x) 4-x^2
A <- integrate(f, -2, 2)$value
My <- integrate(function(x) x*f(x), -2, 2)$value
Mx <- integrate(function(x) 0.5*f(x)^2, -2, 2)$value
cat("Area:", A, "\n")
cat("Centroid x:", My/A, "\n")
cat("Centroid y:", Mx/A, "\n")
