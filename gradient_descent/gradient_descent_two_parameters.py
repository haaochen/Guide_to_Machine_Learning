heights = [3.2,1.9,1.4]
weights = [2.9,2.3,0.5]
learning_rate_int = 0.01
learning_rate_slope = 0.01
current_intercept = 0
current_slope = 0.5
iterations = 1000

assert len(heights) == len(weights), "Please enter an equal number of measurements for heights and weights"
measurement_length = len(heights)

for i in range(iterations):
    cost_function_int = 0
    cost_function_slope = 0
    for i in range(measurement_length):
        cost_function_int += (-2 * (heights[i] - (current_intercept + current_slope * weights[i])))
        cost_function_slope += (-2 * weights[i] * (heights[i] - (current_intercept + current_slope * weights[i])))
            
    step_size_int = cost_function_int * learning_rate_int
    step_size_slope = cost_function_slope * learning_rate_slope
    new_intercept = current_intercept - step_size_int
    new_slope = current_slope - step_size_slope
    current_intercept = new_intercept
    current_slope = new_slope

    print("The current intercept is now: {0} with an intercept step size of: {1}".format(current_intercept, step_size_int))
    print("The current slope is now: {0} with a slope step size of: {1}".format(current_slope, step_size_slope))

