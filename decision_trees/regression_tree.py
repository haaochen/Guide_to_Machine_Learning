'''
This script demonstrates a first iteration at regression trees that uses drug doses to predict drug effectiveness in percentages
'''
#This is a list of tuples that represent drug amount, and drug effectiveness (percentage), respectively in each tuple
doses_effectiveness = [(1,0),(3,0),(8,0),(9,3),(12,10),(14,100),(19,100),(23,100),(25,100),(28,73),(28.5,60),(29,55),(29.5,50),(30,47),(31.5,5),(33,0),(37,0),(30,0)]

#In a while loop, collect two values at a time, get the average of values above and below the average of the two point, then determin SSR. Once we reach a minimum SSR, we stop
#This will find a local minimum but is not guaranteed to find the global minimum. This example is planned such that the local minimum is the correct value
ssr_list = []

for i in range(len(doses_effectiveness) - 1):
    ssr_below = 0
    ssr_above = 0
    avg = (doses_effectiveness[i][0] + doses_effectiveness[i+1][0])/2
    values_below_root = [d for d in doses_effectiveness if d[0] < avg]
    values_above_root = [d for d in doses_effectiveness if d[0] >= avg]
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
print("This means the list splits at values less than: {0}".format(doses_effectiveness[ssr_list.index(min(ssr_list)) + 1]))