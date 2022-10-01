'''
This program calculates the sum of squared residuals. This calculation is useful in determining if a model's predictions are trustworthy.
Residual = Observed - Predicted
SSR = sum(Observed - Predicted)^2
The sum of squared residuals is the sum of the squared difference between the observed and predicted values
'''

def sumOfSquaredResiduals(obs, pres, base_ssr, total_length):
    for i in range(total_length):
        base_ssr += (obs[i] - pres[i])**2
    return base_ssr

def meanSquaredError(c_ssr, total_length):
    mse = c_ssr/total_length
    return mse

observations = list(map(float, input("Please enter the observations, separated by a single space \n").split()))
predictions = list(map(float, input("Please enter the predictions, separated by a single space \n").split()))
assert len(observations) == len(predictions), "The number observations and predictions is different. Please enter the the same number of observations and predictions"
total_len = len(observations)
SSR = 0

calc_ssr = sumOfSquaredResiduals(observations, predictions, SSR, total_len)
calc_mse = meanSquaredError(calc_ssr, total_len)


print("The Sum of Squared Residuals is: ", calc_ssr)
print("The Mean Squared Error is: ", calc_mse)