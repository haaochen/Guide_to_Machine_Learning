'''
This script demonstrates regression trees that uses drug doses to predict drug effectiveness. I will use an iterative structure for this example
'''
#This is a list of tuples that represent drug amount, and drug effectiveness (percentage), respectively in each tuple
doses = [(1,0),(3,0),(8,0),(9,3),(12,10),(14,100),(19,100),(23,100),(25,100),(28,73),(28.5,60),(29,55),(29.5,50),(30,47),(31.5,5),(33,0),(37,0),(30,0)]

#In a while loop, collect two values at a time, get the average of values above and below the average of the two point, then determin SSR. Once we reach a minimum SSR, we stop
#This will find a local minimum but is not guaranteed to find the global minimum. This example is planned such that the local minimum is the correct value
while (True):
    ssr_below = 0
    ssr_above = 0
    ssr = 0
    for i in range(len(doses)):
        avg = (doses[i][0] + doses[i+1][0])/2
        values_below_root = [d for d in doses if d[0] < avg]
        values_above_root = [d for d in doses if d[0] >= avg]
        num_of_values_below_avg_dose = len(values_below_root)
        num_of_values_above_avg_dose = len(values_above_root)
        avg_values_below_root = sum([y for x,y in values_below_root])/num_of_values_below_avg_dose
        avg_values_above_root = sum([y for x,y in values_above_root])/num_of_values_above_avg_dose
        #calculate SSR
        for i in range(num_of_values_below_avg_dose):
            ssr_below += (doses[i][1] - avg_values_below_root)**2
            print(ssr_below)
        begin_index_for_above_values = len(doses) - (len(doses) - num_of_values_above_avg_dose)
        for i in range(begin_index_for_above_values, len(doses)):
            ssr_above += (doses[i][1] - avg_values_above_root)**2
            print(ssr_above)
        ssr_current = ssr_below + ssr_above
        print(ssr_current)
        if ssr_current < ssr:
            ssr = ssr_current
        else:
            break
    break
        
