r <- function(theta) 2*(1+cos(theta))
dr <- function(theta) -2*sin(theta)
A <- integrate(function(t) 0.5*r(t)^2,0,2*pi)$value
L <- integrate(function(t) sqrt(r(t)^2+dr(t)^2),0,2*pi)$value
cat("Area:",A," vs ",6*pi,"\n")
cat("Length:",L," vs ",16,"\n")
