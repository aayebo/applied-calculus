x <- seq(12, 20, length.out=201)
f <- sqrt(x)
L <- 4 + (x-16)/8
plot(x, f, type="l", col="blue")
lines(x, L, col="red", lty=2)
cat("Approximation:", 4.05, "\n")
cat("Absolute error:",
    abs(sqrt(16.4)-4.05), "\n")
