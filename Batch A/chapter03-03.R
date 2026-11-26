f <- sin
x <- 1
h <- 10^(-seq(1, 7))
forward <- (f(x+h)-f(x))/h
central <- (f(x+h)-f(x-h))/(2*h)
print(data.frame(h,
  err_forward=abs(forward-cos(x)),
  err_central=abs(central-cos(x))))
