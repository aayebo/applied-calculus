f <- function(t) exp(-t) - 0.2
solution <- uniroot(f, interval = c(0, 5))
solution$root
-log(0.2)                    # Exact comparison
