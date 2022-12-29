'''
The purpose of this script is to demonstrate gradient descent that optimizes one parameter
Derivative of the Loss Function (in this case, sum of squared residuals) that will be used: -2 * (Height - (intercept + 0.64 * Weight))
We do not have to do this for Linear Regression but this is an example of using gradient descent
We divide the derivative of the SSR by the derivative of the intercept for each measurement and add the values
The result is the magnitude of the step we should take towards the minimum. We multiply this by the learning rate to avoid taking too large of a step
The learning rate starts large and gets smaller. Cross validation can determine the learning rate
Once we calculate the new intercept, we continue until we get close to zero or we have completed iterations
'''

heights = [3.2,1.9,1.4]
weights = [2.9,2.3,0.5]
learning_rate = 0.1
current_intercept = 0
iterations = 1000

assert len(heights) == len(weights), "Please enter an equal number of measurements for heights and weights"
measurement_length = len(heights)

for i in range(iterations):
    cost_function = 0

    for i in range(measurement_length):
        cost_function += (-2 * (heights[i] - (current_intercept + 0.64 * weights[i])))
            
    step_size = cost_function * learning_rate
    new_intercept = current_intercept - step_size
    current_intercept = new_intercept
    print("current step size is: {} and the new intercept is: {}".format(step_size, current_intercept))
    if step_size == 0:
        print("The current step size is equal to zero")
        break

