rate <- function(t) 2 + 0.5*t
A <- function(x) integrate(rate, 0, x)$value
x <- seq(0, 4, length.out=101)
plot(x, vapply(x, A, numeric(1)), type="l", lwd=2,
     xlab="Time (hours)", ylab="Accumulated volume (L)")
cat("Volume after 4 hours:", A(4), "L\n")
h <- 1e-4
cat("Approx derivative at t=2:", (A(2+h)-A(2-h))/(2*h), "\n")
cat("Rate at t=2:", rate(2), "L/hour\n")
