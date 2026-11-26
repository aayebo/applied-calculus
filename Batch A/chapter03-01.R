f <- function(x) x^2 + 2*x
a <- 3
h <- 10^(-seq(1, 6))
secant <- (f(a+h)-f(a))/h
print(data.frame(h, secant,
                 error=abs(secant-8)))
