a <- 1
speed <- function(t) sqrt((a*(1-cos(t)))^2+(a*sin(t))^2)
L <- integrate(speed,0,2*pi)$value
cat("Numerical length:",L," Exact length:",8*a,"\n")
