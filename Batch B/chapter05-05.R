top <- function(x) 4-x^2
bottom <- function(x) x
alpha <- (-1+sqrt(17))/2
area <- integrate(function(x) top(x)-bottom(x), 0, alpha)$value
cat("Intersection:", alpha, "Area:", area, "\n")
x <- seq(0, alpha, length.out=200)
plot(x, top(x), type="l", lwd=2, ylim=c(0,4),
     xlab="x", ylab="y")
lines(x, bottom(x), lwd=2, lty=2)
