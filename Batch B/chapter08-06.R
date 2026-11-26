f <- function(x) 1/x^3
for (upper in c(4, 10, 100, 1000)) {
  value <- integrate(f,2,upper)$value
  cat('Upper limit:',upper,' integral:',round(value,8),
      ' target:',1/8,'\n')
}
# Numerical evidence complements the exact p-test.
