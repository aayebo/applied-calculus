N <- c(5, 10, 20, 50, 100)
upper <- 1/(2*N^2)
lower <- 1/(2*(N+1)^2)
print(data.frame(N, lower, upper))
cat("Smallest N for upper error < 0.001:",
    which(1/(2*(1:100)^2) < 0.001)[1], "\n")
