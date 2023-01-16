'''
This script demonstrates regression trees.
'''
#This is a list of tuples that represent drug amount, and drug effectiveness, respectively in each tuple
doses = [(1,0),(3,0),(8,0),(9,3),(12,10),(14,100),(19,100),(23,100),(25,100),(28,73),(28.5,60),(29,55),(29.5,50),(30,47),(31.5,5),(33,0),(37,0),(30,0)]

#take the average of the first two doses - this will be the root node
avg = (doses[0][0] + doses[1][0])/2

#Put the average of effectiveness with doses less than avg to the left of the root node and the avg effectiveness of the doses >= avg to the right
values_below_root = [d for d in doses if d[0] < avg]
values_above_root = [d for d in doses if d[0] >= avg]
num_of_values_below_avg_dose = len(values_below_root)
num_of_values_above_avg_dose = len(values_above_root)
avg_values_below_root = sum([y for x,y in values_below_root])/num_of_values_below_avg_dose
avg_values_above_root = sum([y for x,y in values_above_root])/num_of_values_above_avg_dose
print("For the values < avg, the prediction is pretty good at: {0} since the effectiveness is zero for these doses\nFor the values > avg, the predictions are not so good at: {1}".format(avg_values_below_root, avg_values_above_root))