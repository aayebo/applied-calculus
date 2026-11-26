t <- seq(0, 2*pi, length.out=600)
a <- 1
x <- a*(t-sin(t)); y <- a*(1-cos(t))
plot(x,y,type="l",asp=1,xlab="x",ylab="y",main="Cycloid")
idx <- seq(1,length(t),length.out=15)
points(x[round(idx)],y[round(idx)],pch=19,col="red")
