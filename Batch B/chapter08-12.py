for upper in [4,10,100,1000]:
    value = 1/8-1/(2*upper**2)
    print('Upper:',upper,'Truncated integral:',round(value,8),
          'Limit:',1/8)
# This is an exact truncated antiderivative, not numerical quadrature.
