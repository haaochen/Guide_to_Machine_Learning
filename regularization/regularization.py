'''
This script demonstrates performs calculations that will result in ridge/l2 regularization. SSR + lambda x slope**2
The goal is to pick the minimal ridge score
'''

#Ridge Regularization
print("Ridge Regularization...")
SSR_fit = 0 #fitting trining data perfectly
slope_fit = 1.3
lmda_fit = 1
score_fit = SSR_fit + lmda_fit*slope_fit**2

print("The score for a line that fits the training data perfectly is: {0}".format(score_fit))

SSR_no_fit = 0.4 #fitting trining data perfectly
slope_no_fit = 0.6
lmda_no_fit = 1
score_no_fit = SSR_no_fit + lmda_no_fit*slope_no_fit**2
print("The score for a line that does not fit the training data perfectly is: {0}".format(score_no_fit))

#Lasso Regularization
print("Lasso Regularization...")
SSR_fit_l = 0 #fitting trining data perfectly
slope_fit_l = 1.3
lmda_fit_l = 1
score_fit_l = SSR_fit_l + lmda_fit_l*abs(slope_fit_l)

print("The score for a line that fits the training data perfectly is: {0}".format(score_fit_l))

SSR_no_fit_l = 0.4 #fitting trining data perfectly
slope_no_fit_l = 0.6
lmda_no_fit_l = 1
score_no_fit_l = SSR_no_fit_l + lmda_no_fit_l*abs(slope_no_fit_l)
print("The score for a line that does not fit the training data perfectly is: {0}".format(score_no_fit_l))
