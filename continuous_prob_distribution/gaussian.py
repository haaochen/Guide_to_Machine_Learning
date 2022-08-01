'''
This program calculates Gaussian distribution
Determine x given mu and std. Gives likelihood (y-axis), not probability. 
'''

from math import exp, pi, sqrt
def gaussian(x, mu, dev):
    prob = (1/(sqrt(2*pi*pow(dev, 2)))) * exp((-pow((x-mu),2))/2*pow(dev,2))
    return prob

print(gaussian(50,50,1.5))
