theta <- seq(-2.2,2.2,length.out=1000)
par(mfrow=c(1,3))
for(e in c(0.5,1,1.4)) {
  den <- 1+e*cos(theta)
  keep <- den > 0.08
  r <- 3/den
  x <- r*cos(theta); y <- r*sin(theta)
  x[!keep] <- NA; y[!keep] <- NA
  plot(x,y,type="l",asp=1,xlab="x",ylab="y",
       main=paste("eccentricity =",e))
}
par(mfrow=c(1,1))
