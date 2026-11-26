f <- function(x) x^3 - 3*x
fp <- function(x) 3*x^2 - 3
fpp <- function(x) 6*x
x <- seq(-2,2,length.out=500)
par(mfrow=c(3,1), mar=c(3,4,2,1))
plot(x,f(x),type="l",main="Function")
plot(x,fp(x),type="l",main="First derivative"); abline(h=0,lty=2)
plot(x,fpp(x),type="l",main="Second derivative"); abline(h=0,lty=2)
par(mfrow=c(1,1))
