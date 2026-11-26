area <- function(x) sqrt(3)/4 * (2-x)^2
volume <- integrate(area, 0, 2)$value
cat("Triangular cross-section volume:", volume, "\n")
x <- seq(0, 2, length.out=200)
plot(x, area(x), type="l", lwd=2, xlab="Position x",
     ylab="Cross-sectional area A(x)")
