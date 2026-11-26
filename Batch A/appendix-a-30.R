analytic_time <- -log(0.3) / 0.12
numeric_time <- uniroot(function(t) Tmodel(t) - 40,
                        interval = c(0, 30))$root
c(analytic = analytic_time, numerical = numeric_time)
Tmodel(numeric_time)
