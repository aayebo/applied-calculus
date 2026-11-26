q <- function(t) 3 + 0.4*t
midpoint_sum(q, 0, 10, n = 20)
integrate(q, 0, 10)$value
