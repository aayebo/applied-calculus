k <- -log(50/80)/6
half_life <- log(2)/k
cat("Rate:", round(k, 5), "per hour\n")
cat("Half-life:", round(half_life, 2), "hours\n")
stopifnot(abs(80*exp(-k*6) - 50) < 1e-10)
