theta <- seq(0,2*pi,length.out=1200)
par(mfrow=c(1,2))
r <- 2*(1+cos(theta))
plot(r*cos(theta),r*sin(theta),type="l",asp=1,
     xlab="x",ylab="y",main="Cardioid")
r <- 3*cos(2*theta)
plot(r*cos(theta),r*sin(theta),type="l",asp=1,
     xlab="x",ylab="y",main="Four-petal rose")
par(mfrow=c(1,1))
