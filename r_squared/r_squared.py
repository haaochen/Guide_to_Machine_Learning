'''
This program calculates the R Squared value. One on line, separated by whitespace, enter the observation numbers then hit Enter. Next, Enter the 
predicted values of the mean separated by whitespace and hit Enter. Last, enter the predicted values of the model and hit Enter.
'''

def sumOfSquaredResiduals(obs, pres, total_length):
    ssr = 0
    for i in range(total_length):
        ssr += (obs[i] - pres[i])**2
    return ssr

def meanSquaredError(ssr, total_length):
    mse = 0
    mse = ssr/total_length
    return mse

def rSquaredSSR(mean_ssr, fitted_ssr):
    rsssr = 0
    rsssr = (mean_ssr - fitted_ssr)/mean_ssr
    return rsssr

def rSquaredMSE(mean_mse, fitted_mse):
    rsmse = 0
    rsmse = (mean_mse - fitted_mse)/mean_mse
    return rsmse

observations = list(map(float, input("Please enter the observations, separated by a single space \n").split()))
predictions_mean = list(map(float, input("Please enter the mean prediction (enter the mean value for each observation), separated by a single space \n").split()))
predictions_fitted = list(map(float, input("Please enter the model predictions, separated by a single space \n").split()))

assert len(observations) == len(predictions_mean) == len(predictions_fitted), "The number observations and predictions is different. Please enter the the same number of observations, mean predictions and fitted predictions"
total_len = len(observations)

mean_ssr = sumOfSquaredResiduals(observations, predictions_mean, total_len)
fitted_ssr = sumOfSquaredResiduals(observations, predictions_fitted, total_len)

mean_mse = meanSquaredError(mean_ssr, total_len)
fitted_mse = meanSquaredError(fitted_ssr, total_len)

r2_ssr = rSquaredSSR(mean_ssr, fitted_ssr)
r2_mse = rSquaredMSE(mean_mse, fitted_mse)

print("SSR of the mean of the data is: ", mean_ssr)
print("SSR of the model data is: ", fitted_ssr)

print("MSE of the mean of the data is: ", mean_mse)
print("MSE of the model data is: ", fitted_mse)

print("R Squared using SSR is: ", r2_ssr)
print("R Squared using MSE is: ", r2_mse)
