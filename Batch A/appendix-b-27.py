threshold = 35
analytic_time = np.log((initial-ambient) /
                       (threshold-ambient)) / k
numerical_time = optimize.brentq(
    lambda t: temp(t)-threshold, 0, 30)
print("Analytic:", analytic_time)
print("Numerical:", numerical_time)
print("Check:", temp(numerical_time))
