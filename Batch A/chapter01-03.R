x <- seq(-2, 5, length.out = 500)
plot(x, x^2, type = "l", col = "navy",
     ylim = c(-5, 10), xlab = "x", ylab = "y")
lines(x, -2*(x - 3)^2 + 4, col = "firebrick")
points(3, 4, pch = 19)
legend("topleft", c("x^2", "-2(x-3)^2+4"),
       col = c("navy", "firebrick"), lty = 1)
