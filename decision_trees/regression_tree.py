'''
This script demonstrates a first iteration at regression trees that uses drug doses to predict drug effectiveness in percentages
'''
#This is a list of tuples that represent drug amount, and drug effectiveness (percentage), respectively in each tuple
doses_effectiveness = [(1,0),(3,0),(8,0),(9,3),(12,10),(14,100),(19,100),(23,100),(25,100),(28,73),(28.5,60),(29,55),(29.5,50),(30,47),(31.5,5),(33,0),(37,0),(30,0)]
print("This is the list of doses and effectiveness: {0}".format(doses_effectiveness))

#In a while loop, collect two values at a time, get the average of values above and below the average of the two point, then determin SSR. Once we reach a minimum SSR, we stop
#This will find a local minimum but is not guaranteed to find the global minimum. This example is planned such that the local minimum is the correct value
split_min = 6

def regression_tree(de_list):
    print("Calling the regression function...")
    ssr_list = []
    for i in range(len(de_list) - 1):
        ssr_below = 0
        ssr_above = 0
        avg = (de_list[i][0] + de_list[i+1][0])/2
        values_below_root = [d for d in de_list if d[0] < avg]
        values_above_root = [d for d in de_list if d[0] >= avg]
        num_of_values_below_avg_dose = len(values_below_root)
        num_of_values_above_avg_dose = len(values_above_root)
        avg_value_below_root = sum([y for x,y in values_below_root])/num_of_values_below_avg_dose
        avg_value_above_root = sum([y for x,y in values_above_root])/num_of_values_above_avg_dose
        for j in values_below_root:
            ssr_below += (j[1] - avg_value_below_root)**2
        for k in values_above_root:
            ssr_above += (j[1] - avg_value_above_root)**2
        ssr_current = ssr_below + ssr_above
        ssr_list.append(ssr_current)
    print("The list of SSR values from the above list of dosages and effectiveness percentages is: {}".format(ssr_list))
    print("The lowest value of the SSR values is: {0}".format(min(ssr_list)))
    print("This means the list splits at values before: {0}".format(de_list[ssr_list.index(min(ssr_list)) + 1]))
    print("Finished the regression function...")
    return ssr_list

ssr_list = regression_tree(doses_effectiveness)
values_to_the_left = doses_effectiveness.index(doses_effectiveness[ssr_list.index(min(ssr_list)) + 1])
print("Since there are {0} values to the left of the split value. This might lead to overfitting if we apply regression to those values. We will not split those values further as the minimum number of values to continue on either side is {1}".format(values_to_the_left, split_min))
low_average_effectiveness = 0
for i in range(values_to_the_left):
    low_average_effectiveness += doses_effectiveness[i][1]
low_average_effectiveness = low_average_effectiveness/values_to_the_left
print("We will add a leaf to the left of the split value, composed of the average effectiveness of the remaining values to the left of the split value. The average effectiveness for the values to the left of the split value is: {0}%".format(low_average_effectiveness))
print("Lets continue to the right side of the split value and including the split value...")
doses_effectiveness = doses_effectiveness[values_to_the_left:]
print("Let's just take those values into a new list: {0}".format(doses_effectiveness))
print('-'*25)
ssr_list = regression_tree(doses_effectiveness)
split_value = doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]
print("The split value is: {0}".format(split_value))
values_to_the_right = len(doses_effectiveness) - doses_effectiveness.index(doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]) - 1
high_average_effectiveness = 0
for i in range(-1,values_to_the_right + 1,-1):
    high_average_effectiveness += doses_effectiveness[i][1]
high_average_effectiveness = high_average_effectiveness/values_to_the_right
print("Since there are {0} values to the right, which is less than our split minimum of {1}, then we calculate the average effectiveness for those values including the split value and make a leaf on the left of our split value because we want to test for values more than or equal to the split value: {2}%".format(values_to_the_right, split_min, high_average_effectiveness))
print("Lets remove those values from the list to clean things up...and create yet another list on which to operate, which include the remaining values")
doses_effectiveness = doses_effectiveness[:-values_to_the_right]
print("The remaining list is: {0}".format(doses_effectiveness))
print('-'*25)
ssr_list = regression_tree(doses_effectiveness)
split_value = doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]
print("The split value is: {0}".format(split_value))
values_to_the_right = len(doses_effectiveness) - doses_effectiveness.index(doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]) - 1
high_average_effectiveness = 0
for i in range(doses_effectiveness.index(split_value) + 1,len(doses_effectiveness)):
    high_average_effectiveness += doses_effectiveness[i][1]
high_average_effectiveness = high_average_effectiveness/values_to_the_right

print("There are only three values on the right side of the split value {0}: {1} '\n'So we average the effectiveness and make that average a leaf: {2}%".format(split_value,doses_effectiveness[doses_effectiveness.index(split_value) + 1:], high_average_effectiveness))
doses_effectiveness = [x for x in doses_effectiveness[0:len(doses_effectiveness) - values_to_the_right]]
print("The remaining items in the list are: {0}".format(doses_effectiveness))
print('-'*25)
print("Let's perform regression on the remaining list...")
ssr_list = regression_tree(doses_effectiveness)
split_value = doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]
print("The split value is: {0}".format(split_value))
values_to_the_right = len(doses_effectiveness) - doses_effectiveness.index(doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]) - 1
high_average_effectiveness = 0
for i in range(doses_effectiveness.index(split_value) + 1,len(doses_effectiveness)):
    high_average_effectiveness += doses_effectiveness[i][1]
high_average_effectiveness = high_average_effectiveness/values_to_the_right
print("There is only one value on the right side of the split value {0}: {1} '\n'So we average the effectiveness and make that average a leaf: {2}%".format(split_value,doses_effectiveness[doses_effectiveness.index(split_value) + 1:], high_average_effectiveness))
doses_effectiveness = [x for x in doses_effectiveness[0:len(doses_effectiveness) - values_to_the_right]]
print("The remaining items in the list are: {0}".format(doses_effectiveness))
print('-'*25)
print("Let's perform regression on the remaining list...")
ssr_list = regression_tree(doses_effectiveness)
split_value = doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]
print("The split value is: {0}".format(split_value))
values_to_the_right = len(doses_effectiveness) - doses_effectiveness.index(doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]) - 1
doses_effectiveness = [x for x in doses_effectiveness[0:len(doses_effectiveness) - 1]]
final_avg_sum = 0
for i in range(len(doses_effectiveness)):
    final_avg_sum += doses_effectiveness[i][1]
average_effectiveness = final_avg_sum/len(doses_effectiveness)
print("Since there are no values to the right of the split value, we prune this value and this remaining values are: {0}".format(doses_effectiveness))
print("Since there are less than the minimum number of values needed, we end our regression here. We can see that values for doeses less than 14 and more than 28 have been pruned so values for doses between 14 and 28 provide the highest effectiveness. In a perfect example, we would have been left with only 100 percent effective doeses but we wanted to make up these values for experiments sake. The average effectiveness of these doese within the testing threshold is: {0}%".format(average_effectiveness))
