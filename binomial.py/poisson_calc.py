'''
Poisson is used to determine the probability of event happening in discrete units of time
lambda is the current rate of the event, we want to calculate the probability of the event happening at the rate of x
'''
from math import factorial, exp
from operator import neg

def poisson(l, x):
    prob = exp(neg(l)) * pow(l,x)/factorial(x)
    return prob

print(poisson(10, 8))
