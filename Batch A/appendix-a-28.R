f <- function(x) x^3 - 3*x + 2
L <- function(x) 4 + 9*(x - 2)
x <- seq(1.2, 2.6, length.out = 300)
plot(x, f(x), type = "l", lwd = 2,
     xlab = "x", ylab = "y",
     main = "Function and tangent line")
lines(x, L(x), lty = 2, lwd = 2)
points(2, 4, pch = 19)
legend("topleft", c("f(x)", "Tangent at x=2"),
       lty = c(1, 2), lwd = 2, bty = "n")
central_diff(f, 2)
