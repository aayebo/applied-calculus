time <- c(0, 5, 10, 15, 20, 25)
temp <- c(82.0, 69.0, 58.9, 51.0, 44.8, 39.8)
fit <- lm(log(temp - 22) ~ time)
k <- -unname(coef(fit)[2])
pred <- 22 + 60*exp(-k*time)
print(data.frame(time, observed=temp, predicted=pred,
                 residual=temp-pred))
plot(time, temp, xlab="Time (min)", ylab="Temperature (C)")
curve(22 + 60*exp(-k*x), from=0, to=30, add=TRUE)
