'''
This is a script that calculates sensitivity and specificity from a datafram that holds values of a confusion matrix
'''

import pandas as pd

#Values for confusion matrix
TP_B = 142
FN_B = 29
FP_B = 22
TN_B = 110

TP_L = 139
FN_L = 32
FP_L = 20
TN_L = 112


confusion_matrix_data_bayes = [[TP_B,FN_B,FP_B,TN_B]]
confusion_matrix_logistic_regression = [[TP_L,FN_L,FP_L,TN_L]]

#Construct Dataframe in Pandas for visualization purposes
confusion_matrix_b = pd.DataFrame(confusion_matrix_data_bayes,columns=['True Positive', 'False Negative','False Positive','True Negative'],dtype=int)
confusion_matrix_l = pd.DataFrame(confusion_matrix_logistic_regression,columns=['True Positive', 'False Negative','False Positive','True Negative'],dtype=int)

confusion_matrix_b['True Positive'] = TP_B
confusion_matrix_b['False Negative'] = FN_B
confusion_matrix_b['False Positive'] = FP_B
confusion_matrix_b['True Negative'] = TN_B

confusion_matrix_l['True Positive'] = TP_L
confusion_matrix_l['False Negative'] = FN_L
confusion_matrix_l['False Positive'] = FP_L
confusion_matrix_l['True Negative'] = TN_L


print("The confusion matrix for naive bayes is: \n{0}".format(confusion_matrix_b))
print("The confusion matrix for logistic regression is: \n{0}".format(confusion_matrix_l))


#Create dataframe for sensitivity andspecificity and make calculations
sensitivity = TP_B/(TP_B+FN_B)
specificity = TN_L/(TN_L+FP_L)
results = [[sensitivity,specificity]]
results_matrix = pd.DataFrame(results,columns=['sensitivity','specificity'],dtype=float)
results_matrix['sensitivity'] = sensitivity
results_matrix['specificity'] = specificity

print("the results are: \n{0}".format(results_matrix))
print("The results of these two models show that Naive Bayes is '{0}%' better at the true positives than logistic regression and logistic regression is '{1}%' better at true negatives than naive bayes\n".format(round(sensitivity*100,2),round(specificity*100,2)))

bayes_precision = TP_B/(TP_B+FP_B)
logistic_regression_precision = TP_L/(TP_L+FP_L)

print("Of the predicted positive values for Naive Bayes, '{0}%' were correct. Of the predicted positive values for logistic regression, '{1}' are correct. The highest percentage wins.\n".format(round(bayes_precision*100,2), round(logistic_regression_precision*100,2)))

bayes_false_positive = FP_B/(FP_B+TN_B)
logistic_regression_false_positive = FP_L/(FP_L+TN_L)

print("The percentage of negatives that were incorrectly classified is '{0}%' for Naive Bayes. The percentage of negatives that were incorrectly classified is, '{1}' for logistic regression".format(round(bayes_false_positive*100,2), round(logistic_regression_false_positive*100,2)))
