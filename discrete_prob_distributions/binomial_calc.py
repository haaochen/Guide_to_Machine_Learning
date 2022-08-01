'''
This short program calculates the Binomial Distribution. It determines the probability of 'x', given 'n', 'p'
This calculates the probability that x out of n things meet the p probability
'''
from math import factorial
def binomial(x,p,n):
    prob = (factorial(n)/(factorial(x) * factorial(n-x))) * pow(p,x) * pow(1-p, n-x)
    return prob
    
print(binomial(2.00,0.7,3.00))




