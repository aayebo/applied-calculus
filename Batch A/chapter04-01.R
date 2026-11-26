f <- function(x) x^3 - 3*x + 1
fp <- function(x) 3*x^2 - 3
x <- seq(-2, 2, length.out = 401)
plot(x, f(x), type = "l", lwd = 2,
     xlab = "x", ylab = "f(x)", main = "Extrema")
points(c(-2,-1,1,2), f(c(-2,-1,1,2)), pch = 19)
candidates <- c(-2,-1,1,2)
data.frame(x=candidates, value=f(candidates),
           derivative=fp(candidates))
