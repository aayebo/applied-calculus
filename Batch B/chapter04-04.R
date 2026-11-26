h <- 10^(-seq(1,15,by=2))
naive <- (exp(h)-1)/h
stable <- expm1(h)/h
print(data.frame(h=h, naive=naive, stable=stable))
