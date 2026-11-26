f <- function(x) 1/(x - 1)
left <- seq(-1, 0.95, length.out = 400)
right <- seq(1.05, 3, length.out = 400)
plot(left, f(left), type = "l", col = "navy",
     xlim = c(-1, 3), ylim = c(-15, 15),
     xlab = "x", ylab = "f(x)")
lines(right, f(right), col = "firebrick")
abline(v = 1, lty = 2)
