# Guide_to_Machine_Learning

Coding the examples from the StatQuest Illustrated Guide to Machine Learning (Python)

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
