# Guide_to_Machine_Learning

Coding the examples from the StatQuest Illustrated Guide to Machine Learning (Python). The code in this repository is my own, however, the credit for the material that is the inspiration for this repository goes to Josh Starmer, Ph.D, author of The StatQuest Illustrated Guide to Machine Learning. Please consider purchasing a copy of this excellent book for your own learning.

## Discrete Probability Distributions

- This folder contains the calculation of the Binomial Distribution and the Poisson Distribution. The calculations are used for discrete probability distributions and can be used when not enough data is present to fill in the gaps in, for example, a histogram.

## Continuous Distributions

- The Gaussian distribution is used for continuous data. In order to calculate the Gaussian distribution, you need the mean and the standard deviation of the data.

- Exponential distributions are good for determining the likelihood of the time that passes between events.

- Uniform distributions can be used to generate random numbers (e.g. between 0 and 1)

- Probability distributions are types of models that allow us to give approximations as if we had an unlimited amount of data.

## Models

- Models, such as the equation of a line, can tell us about data we have not measured yet.

- Since models are only approximations, we need to measure their quality - their distance from their predictions, using statistics

- Sum of squared residuals: One way to determine the quality of a models predictions

- The issue with the Sum of Squared Residuals is that it only tells us the residuals, not that a model is better or worse that another

- Mean Squared Error (average of SSR) can be used to compare to models with different sized data sets

- MSE can seem to give differing results depending on the scale of the data and the size of the dataset. R Squared solves this problem

- R Squared compares the SSR or MSE about the mean to the SSR or MSE of our model. Values are between 0 and 1 and the closer to 1 means the better the fit

- R squared = (SSR(mean) - SSR(fitted line))/SSR(mean)

- This equation tells us what percentage of residuals shrank around the mean when we used the fitted line

- When SSR(mean) = SSR(fitted), then both models are equally good at fitting the data. When SSR(fitted) = 0, R Squared = 1, the fitted line fits the data perfectly

- ANY 2 points have a R Squared equal to 1 - just draw a line through them.

- R Squared can be calculated for anything we can calculated the SSR for. R Squared can be negative if the shape of the model is different.

- R Squared tells us the percent reduction in residuals when we use a model versus the mean

- p-values tell use how confident we can be in our predictions. A common threshold is .05

- When talking about p-values, a value less than the threshold tells us that there is a difference but not how different. Smaller values do not imply that the difference is large. The closer to zero, the more confident that there is a difference at all.

- Fischer's Exact Test can be used to derive p-values

## Linear Regression

- Linear Regression fits a line to the data that minimizes the SSR. It selects the line, the intercept and the slope that minimizes SSR

- Goal of linear regression is to find the lowest SSR at the bottom of the curve. 

- You can use the derivative of the curve to find the lowest point and solve for where the derivative is equal to 0

- The above would be an analytical solution, which work well for certain situations

- You can also use gradient descent (an iterative method) to find the optimal slope and y-axis intercept

- Iterative methods start with a guess for the value then goes into a loop that improves the guess one small step at a time

- Linear regression can be used to create Linear Models

- Linear Models allow us to use discrete dat ato predict something continuous or to used discrete data with continuous data

## Gradient Descent

- Sometimes there is no analytical solution to fit a model to data. Gradient descent starts with a guess and improves over time towards an optimal solution.

- A loss or cost function is a function that we want to minimize when optimizing a model to fit the data. Sometimes, a loss function will refer to a function applied to ony one data point and the term Cost Function to specifically refer to a function applied to all of the data. 

- You can plot the loss function as a function of the y-axis. The answer of when to stop comes from the derivative of the curve, which tells us the slope of any tangent line that touches it. A steeper line (larger tangent) suggests we're relatively far form the bottom of the curve so we need to take a larger step. A negative derivative tells us we need to take a step to the right to get closer to the lowest SSR. A smaller value suggests that we are relatively close to the bottom of the curve, so take a small step. A positive derivative tells us tha twe need to ttake a step to the left to get closer to the lowest SSR (loss function)

- One way to take the derivative is the Chain Rule. The chain rule links the residual to the SSR by rewriting the SSR as a function of the residual

- When there are many parameters, use stochastic gradient descent becuase gradient descent can be slow for big data. Stochastic gradient descent randomly picks one datapoint per step so that only one term is computed per derivative for each iteration.

- Gradient Descnet may not always find the global optimal value in a graph of data that results in multiple local minimums. To avoid this, try using different random numbers to initialize the parameters that we want to optimize, Fiddle around with step size to make it a little larger, or use stochastic gradient descent to increase the randomness.

## Logistic Regression

- Logistic regression comes into play when we want to classify something continuous. Logistic regression is can be thought of as a logistic classifier. the y-axis on a logistic regression graph represents probability. Probabilities have a threshold, usually 0.5

- Likelihoods are use to evaluate how a statistical model fits the dataset. Likelihoods are used instead of SSR for logistic regression

- Calculate the likelihood for the entire model by multiplying likelihoods together. When fitting multiple models, the model with the maximum likelihood is the optimal model. Underflow can happen when multiplying small numbers if the computer is not capable of storing the result. To avoid underflow, add logarithms.

- Weaknesses in logistic regression include that there is an assumption that there is a relationship between the both variables. We assume that an s-shaped model will mostly fit the data. If not, then we need to use another model.

## Naive Bayes

- Naive Bayes is a simple but very effective classifier. It uses prior probability (an initial guess) multiplied by the probabilities of seeing desired results, given a certain condition. Then the same for undesired results and compare.

- Most common Naive bayes is multinomial Naive Bayes.

- We usually derive prior probabilities from the training data. 

- Naive Bayes is naive because it ignores word order and phrasing - it considers each word independently.

- Missing data can be an issue as desired data may only appear in one category in the training data. Because of this, the desired data will always be categorized into one category. Naive Bayes eliminates this problem by adding a pseudocount to each word.

- Naive Bayes works well for discrete data. Continuous data makes use of Gaussian Naive Bayes

- If the data is continuous but not Gaussian, we can use any statistical distribution in combination with Naive Bayes, but it willbe known by a different name (e.g. Exponential Naive Bayes)

- Multinomial Naive Bayes and Gaussian Naive Bayes can be used together when necessary if the data is both continuous and discrete

## Assessing Model Performance

- When assessing which model performs better, one of the tools used is a confusion matrix, which identifies the different outcomes and the predicted outcome in a grid. The highest score in each row determines how well the model performed for that condition. Whent he actual and predectied values are both YES, then that is a true positive. When the actual value is YES and the predicted value is NO, then that is a false negative.
WHen the actual value is NO and the predicted value is YES then that is a false positive. When the actual value is NO and the predicted value is no, then that is a true negative. The confusion matrix contians the square of the number of outcomes rows and columns. There is no standard for creating a confusion matrix so make sure that you read the documentation for how to read a confusion matrix before interpreting results.

- Sensitivity and Specificity can help us determine how much better a model is than another model at predictions.

- True positive rate = Recall = Sensitivity

- Confusion matrices can changed based on the threshold for classification. If it is important to get every True Positive then the threshold will be lower. If it is important to get all of the true negatives, then the threshold will be higher. We will end up with many confusion matrices if we were to test at many thresholds.Receiver Operating characteristic (ROC) graphs help to identify a good classification threshold. The y-axis indicates the number of positive predictions that were correctly classified. The x-axis indicates the number of negative predictions that were incorrectly classified. A diagonal line represents that TP rate = FP rate

- While ROC graphs are great for selecting a threshold, AUC graphs compare how one model performs vs. another. This is a good option if we have multiple models (more than 2 or so). The model with the highest AUC is the most accurate.

- ROC graphs make any model that predicts No 100% of the time look relaly good. Precision recall graphs are an alternative for imbalanced data. In a precision recall graph, precision is on the x-axis and recall is on the y-axis. It works because precision does not includ the number of true negatives.

## Regularization - Preventing Overfitting

- The more flexible a machine learning method is, the easier it is to overfit the Training Data. This will allow a model to fit the training data very well but make horrible predictions on the New Data. When this happens we say that the model has los bias and high variance. We can solve this problem with regularization

- Ridge regularization/L2 Regularization owrks by minimizing SSR and a penalty that's proportional to the square of the slope. If the lamba is 0, then the new line derived form ridge regularization is not different than a line tha tminimizes the SSR/ As lambda grows, the line slope decreases. There is no good way to determin what the best lambda will be so we pick a bunch of values including 0 and see how well each one performs using cross validation. 

- If a model includes 4 parameters, the th eridge penalties would include the sum of the squares of the 4 slopes associated with those variables. The Ridge penalty never includes the intercept becuase it does not directly affect how any of the variables predict height. If there is a variable that is not useful in model prediction it will shrink a lot compared to the slope of other variable which will shrink less. Shrinking the useless variable parameter will shrink the penalty without increasing the SSR. Shrinking the useful variables' slopes would increase the SSR.

- Lasso/L1 Regularization/Absolute Value works by taking the absolute value of the parameter

- Ridge regularizaiton can only shrink the parameters to be asymptotically close to 0 but lasso regularization can shrink the parameter all the way down to 0. Ridge and Lasso
 Regularization are frequently combined to get hte best of both worlds. Lasso regularization is usefule when we need to eliminate useless variable and Ridge regularization is useful when we think most of the variables are useful
