'''
This script demonstrates the idea of classification trees in machine learning. Iterative logic could be used but, for the purposes of learning,
and since the outcome is determined to be quick, we will do linear logic
'''
import pandas as pd


#Populate the data
data = [['yes','yes',7,'no'],['yes','no',12,'no'],['no','yes',18,'yes'],['no','yes',35,'yes'],['yes','yes',38,'yes'],['yes','no',50,'no'],['no','no',83,'no']]

#Create the dataframe
df = pd.DataFrame(data,columns=['Loves Popcorn','Loves Soda','Age','Loves Troll 2'])
print(df)
#Pick the right root node by testing different variables. We must choose the variable that is the best at predicting the feelings for troll 2

#Test Loves Popcorn

loves_troll_2_loves_popcorn = len(df.loc[(df['Loves Popcorn'] == 'yes') & (df['Loves Troll 2'] == 'yes')])
hates_troll_2_loves_popcorn = len(df.loc[(df['Loves Popcorn'] == 'yes') & (df['Loves Troll 2'] == 'no')])

#Test hates popcorn

loves_troll_2_hates_popcorn = len(df.loc[(df['Loves Popcorn'] == 'no') & (df['Loves Troll 2'] == 'yes')])
hates_troll_2_hates_popcorn = len(df.loc[(df['Loves Popcorn'] == 'no') & (df['Loves Troll 2'] == 'no')])

#Test Loves soda

loves_troll_2_loves_soda= len(df.loc[(df['Loves Soda'] == 'yes') & (df['Loves Troll 2'] == 'yes')])
hates_troll_2_loves_soda = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Loves Troll 2'] == 'no')])

#Test hates soda

loves_troll_2_hates_soda = len(df.loc[(df['Loves Soda'] == 'no') & (df['Loves Troll 2'] == 'yes')])
hates_troll_2_hates_soda = len(df.loc[(df['Loves Soda'] == 'no') & (df['Loves Troll 2'] == 'no')])

print("This are the Loves popcorn tree values.\n Loves Popcorn and Loves Troll 2: {0}\n Loves Popcorn and Hates Troll 2: {1}\n Hates popcorn and Loves Troll 2: {2}\n Hates popcorn and Hates Troll 2: {3}\n".format(loves_troll_2_loves_popcorn, hates_troll_2_loves_popcorn, loves_troll_2_hates_popcorn, hates_troll_2_hates_popcorn))
print("This are the Loves soda tree values.\n Loves Soda and Loves Troll 2: {0}\n Loves Soda and Hates Troll 2: {1}\n Hates Soda and Loves Troll 2: {2}\n Hates Soda and Hates Troll 2: {3}\n".format(loves_troll_2_loves_soda, hates_troll_2_loves_soda, loves_troll_2_hates_soda, hates_troll_2_hates_soda))
print("The tree with the fewest number of impure leaves is decided. In this case, it is the Loves Soda tree. Now we use the Gini Impurity to calculate by how much the trees are different")

#Gini Impurity for each leaf
loves_popcorn_left_gini = 1 - (loves_troll_2_loves_popcorn/(loves_troll_2_loves_popcorn + hates_troll_2_loves_popcorn))**2 - (hates_troll_2_loves_popcorn/(loves_troll_2_loves_popcorn + hates_troll_2_loves_popcorn))**2
loves_popcorn_right_gini = 1 - (loves_troll_2_hates_popcorn/(loves_troll_2_hates_popcorn + hates_troll_2_hates_popcorn))**2 - (hates_troll_2_hates_popcorn/(loves_troll_2_hates_popcorn + hates_troll_2_hates_popcorn))**2

print("The Gini Impurity for Loves Popcorn is: {0}".format(loves_popcorn_left_gini))
print("The Gini Impurity for Hates Popcorn is: {0}".format(loves_popcorn_right_gini))

print("Because there is not the same number of people in each leaf, we take the weighted average of the two leaf impurities for each variable")
total_gini_impurity_popcorn = (((loves_troll_2_loves_popcorn + hates_troll_2_loves_popcorn)/(loves_troll_2_loves_popcorn + hates_troll_2_loves_popcorn + loves_troll_2_hates_popcorn + hates_troll_2_hates_popcorn)) * loves_popcorn_left_gini) + ((loves_troll_2_hates_popcorn + hates_troll_2_hates_popcorn)/(loves_troll_2_loves_popcorn + hates_troll_2_loves_popcorn + loves_troll_2_hates_popcorn + hates_troll_2_hates_popcorn)) * loves_popcorn_right_gini
print("the total Gini Impurity for Loves Popcorn is: {0}".format(total_gini_impurity_popcorn))

loves_soda_left_gini = 1 - (loves_troll_2_loves_soda/(loves_troll_2_loves_soda + hates_troll_2_loves_soda))**2 - (hates_troll_2_loves_soda/(loves_troll_2_loves_soda + hates_troll_2_loves_soda))**2
loves_soda_right_gini = 1 - (loves_troll_2_hates_soda/(loves_troll_2_hates_soda + hates_troll_2_hates_soda))**2 - (hates_troll_2_hates_soda/(loves_troll_2_hates_soda + hates_troll_2_hates_soda))**2
print("The Gini Impurity for Loves Soda is: {0}".format(loves_soda_left_gini))
print("The Gini Impurity for Hates Soda is: {0}".format(loves_soda_right_gini))

total_gini_impurity_soda = (((loves_troll_2_loves_soda + hates_troll_2_loves_soda)/(loves_troll_2_loves_soda + hates_troll_2_loves_soda + loves_troll_2_hates_soda + hates_troll_2_hates_soda)) * loves_soda_left_gini) + ((loves_troll_2_hates_soda + hates_troll_2_hates_soda)/(loves_troll_2_loves_soda + hates_troll_2_loves_soda + loves_troll_2_hates_soda + hates_troll_2_hates_soda)) * loves_soda_right_gini
print("the total Gini Impurity for Loves Soda is: {0}".format(total_gini_impurity_soda))

#In order to calculate the Gini Impurity for Age, we typically sort in order. In this case, all of the ages are already in numerical order
#calculate the averages for all adjacent rows
average_for_each_age = []
for i in range(len(df.Age) - 1):
    average_for_each_age.append((df.Age[i] + df.Age[i+1])/2)

print("The averages for all adjacent rows are: {0}".format(average_for_each_age))

#Calculate the Gini Impurity for each Age Group. If there are ties, we can pick which ever
total_gini_impurities_for_age = []
for avg in average_for_each_age:
    below_age_loves_troll_2 = len(df.loc[(df['Age'] < avg) & (df['Loves Troll 2'] == 'yes')])
    below_age_hates_troll_2 = len(df.loc[(df['Age'] < avg) & (df['Loves Troll 2'] == 'no')])
    above_age_loves_troll_2 = len(df.loc[(df['Age'] > avg) & (df['Loves Troll 2'] == 'yes')])
    above_age_hates_troll_2 = len(df.loc[(df['Age'] > avg) & (df['Loves Troll 2'] == 'no')])
    gini_impurity_below_age = 1 - (below_age_loves_troll_2/(below_age_loves_troll_2 + below_age_hates_troll_2))**2 - (below_age_hates_troll_2/(below_age_hates_troll_2 + below_age_loves_troll_2))**2
    gini_impurity_above_age = 1 - (above_age_loves_troll_2/(above_age_loves_troll_2 + above_age_hates_troll_2))**2 - (above_age_hates_troll_2/(above_age_loves_troll_2 + above_age_hates_troll_2))**2
    total_gini_impurities_for_age.append((((below_age_loves_troll_2 + below_age_hates_troll_2)/(below_age_loves_troll_2 + below_age_hates_troll_2 + above_age_loves_troll_2 + above_age_hates_troll_2)) * gini_impurity_below_age) + ((above_age_loves_troll_2 + above_age_hates_troll_2)/(below_age_loves_troll_2 + below_age_hates_troll_2 + above_age_loves_troll_2 + above_age_hates_troll_2)) * gini_impurity_above_age)

print("The total Gini Impurities for the average of all adjacent rows are: {0}".format(total_gini_impurities_for_age))

#Greedily get the minimum impurity. Get the index so that we can tie back to the averages list and select the age bucket
min_impurity_age = min(total_gini_impurities_for_age)
print("The minimum impurity is: {0}".format(min_impurity_age))
selected_avg_age = average_for_each_age[total_gini_impurities_for_age.index(min_impurity_age)]
print("The corresponding age is: {0}".format(selected_avg_age))

print("the final results of calculating total Gini Impurities is as follows: \nLoves Popcorn: {0}\nLoves Soda: {1}\nAge Less Than {2}: {3}".format(total_gini_impurity_popcorn, total_gini_impurity_soda, selected_avg_age, min_impurity_age))
print("The variable with the lowest Gini Impurity is the root node (Loves Soda)")
print("Once again, the tree for Loves Soda is (Loves Soda, Loves Troll 2/Hates Troll 2 and Hates Soda, Loves Troll 2/Hates Troll 2): {0},{1},{2},{3}\n".format(loves_troll_2_loves_soda, hates_troll_2_loves_soda, loves_troll_2_hates_soda, hates_troll_2_hates_soda))
print("The left side of the tree is impure, so we must pick another variable (either Loves Popcorn or Age < 15). We must calculate the Gini impurities for each of the other variables based on Loves Soda")

#Calcuate the Gini Impurity for Loves Popcorn
loves_soda_popcorn_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Loves Popcorn'] == 'yes') & (df['Loves Troll 2'] == 'yes')])
loves_soda_popcorn_hates_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Loves Popcorn'] == 'yes') & (df['Loves Troll 2'] == 'no')])
loves_soda_hates_popcorn_loves_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Loves Popcorn'] == 'no') & (df['Loves Troll 2'] == 'yes')])
loves_soda_hates_popcorn_hates_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Loves Popcorn'] == 'no') & (df['Loves Troll 2'] == 'no')])
loves_popcorn_gini_left = 1 - (loves_soda_popcorn_troll_2/(loves_soda_popcorn_troll_2 + loves_soda_popcorn_hates_troll_2))**2 - (loves_soda_popcorn_hates_troll_2/(loves_soda_popcorn_hates_troll_2 + loves_soda_popcorn_troll_2))**2
loves_popcorn_gini_right = 1 - (loves_soda_hates_popcorn_loves_troll_2/(loves_soda_hates_popcorn_loves_troll_2 + loves_soda_hates_popcorn_hates_troll_2))**2 - (loves_soda_hates_popcorn_hates_troll_2/(loves_soda_hates_popcorn_hates_troll_2 + loves_soda_hates_popcorn_loves_troll_2))**2
total_gini_impurity_soda_popcorn = (((loves_soda_popcorn_troll_2 + loves_soda_popcorn_hates_troll_2)/(loves_soda_popcorn_troll_2 + loves_soda_popcorn_hates_troll_2 + loves_soda_hates_popcorn_loves_troll_2 + loves_soda_hates_popcorn_hates_troll_2)) * loves_popcorn_gini_left) + ((loves_troll_2_hates_popcorn + hates_troll_2_hates_popcorn)/(loves_soda_popcorn_troll_2 + loves_soda_popcorn_hates_troll_2 + loves_soda_hates_popcorn_loves_troll_2 + loves_soda_hates_popcorn_hates_troll_2)) * loves_popcorn_gini_right
print("The total Gini Impurity for Loves Soda and Loves Popcorn is {0}".format(total_gini_impurity_soda_popcorn))

#Calculate the Gini Impurity for Age < 15
loves_soda_below_age_loves_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Age'] < 15) & (df['Loves Troll 2'] == 'yes')])
loves_soda_below_age_hates_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Age'] < 15) & (df['Loves Troll 2'] == 'no')])
loves_soda_above_age_loves_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Age'] > 15) & (df['Loves Troll 2'] == 'yes')])
loves_soda_above_age_hates_troll_2 = len(df.loc[(df['Loves Soda'] == 'yes') & (df['Age'] > 15) & (df['Loves Troll 2'] == 'no')])
below_age_gini_left = 1 - (loves_soda_below_age_loves_troll_2/(loves_soda_below_age_loves_troll_2 + loves_soda_popcorn_hates_troll_2))**2 - (loves_soda_popcorn_hates_troll_2/(loves_soda_popcorn_hates_troll_2 + loves_soda_popcorn_troll_2))**2
above_age_gini_right = 1 - (loves_soda_above_age_loves_troll_2/(loves_soda_above_age_loves_troll_2 + loves_soda_above_age_hates_troll_2))**2 - (loves_soda_above_age_hates_troll_2/(loves_soda_above_age_hates_troll_2 + loves_soda_above_age_loves_troll_2))**2
total_gini_impurity_below_age = (((loves_soda_below_age_loves_troll_2 + loves_soda_below_age_hates_troll_2)/(loves_soda_below_age_loves_troll_2 + loves_soda_below_age_hates_troll_2 + loves_soda_above_age_loves_troll_2 + loves_soda_above_age_hates_troll_2)) * below_age_gini_left) + ((loves_soda_above_age_loves_troll_2 + loves_soda_above_age_hates_troll_2)/(loves_soda_below_age_loves_troll_2 + loves_soda_below_age_hates_troll_2 + loves_soda_above_age_loves_troll_2 + loves_soda_above_age_hates_troll_2)) * above_age_gini_right
print("The total Gini Impurity for age < 15 is: {0}".format(total_gini_impurity_below_age))

print("Age less than 15 has the lower Gini Impurity. It goes to the left of Loves Soda")