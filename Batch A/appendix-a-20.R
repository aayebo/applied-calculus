time <- c(0, 2, 4, 6, 8)
temperature <- c(82, 68, 58, 50, 44)
cooling <- data.frame(time, temperature)
print(cooling)
plot(cooling$time, cooling$temperature,
     xlab = "Time (min)", ylab = "Temperature (C)",
     pch = 19)
