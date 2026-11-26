f <- function(x) sqrt(5 - 2*x) / (x + 1)
x_left  <- seq(-4, -1.02, length.out = 400)
x_right <- seq(-0.98, 2.5, length.out = 400)
plot(x_left, f(x_left), type = "l", col = "navy",
     xlim = c(-4, 2.5), ylim = c(-12, 12),
     xlab = "x", ylab = "f(x)")
lines(x_right, f(x_right), col = "firebrick")
abline(v = -1, lty = 2)
