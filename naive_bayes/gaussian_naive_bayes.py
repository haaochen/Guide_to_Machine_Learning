'''
This script is a simple example of Gaussian Naive Bayes. There are two sets of existing data, positive reviewers and negative reviewers. Each person in each
data set was tracked based on the amount of popcorn, soda, and candy that they consumed. We will classify the data of a new person based on these data points.
'''
#Create the data structures and populate the data
import pandas as pd
import math as m
import numpy as np

#Existing Data
pos_data = [[24.3,750.7,0.2],[28.2,533.2,50.5],[25.7,300.3,1.2]]
neg_data = [[2.1,120.5,90.7],[4.8,110.9,102.3],[10.2,90.8,95.5]]

#New Data
new_data_to_classify = [20.0,500.0,100]

df_pos = pd.DataFrame(pos_data,columns=['Popcorn (grams)','Soda Pop (ml)','Candy (grams)'],dtype=float)
df_neg = pd.DataFrame(neg_data,columns=['Popcorn (grams)','Soda Pop (ml)','Candy (grams)'],dtype=float)
print("The data from the people that loved the movie are: \n{0}".format(df_pos))
print('\n')
print("The data from the people that did not love the movie are: \n{0}".format(df_neg))

#Calculate the total number of existing people in the data
total_people = df_neg.shape[0] + df_pos.shape[0]
print("The total nubmer of people is: {0}\n".format(total_people))

#Calculate Mean and Std for the columns
pos_mean_pop = df_pos['Popcorn (grams)'].mean()
pos_mean_soda = df_pos['Soda Pop (ml)'].mean()
pos_mean_candy = df_pos['Candy (grams)'].mean()

neg_mean_pop = df_neg['Popcorn (grams)'].mean()
neg_mean_soda = df_neg['Soda Pop (ml)'].mean()
neg_mean_candy = df_neg['Candy (grams)'].mean()

pos_std_pop = df_pos['Popcorn (grams)'].std()
pos_std_soda = df_pos['Soda Pop (ml)'].std()
pos_std_candy = df_pos['Candy (grams)'].std()

neg_std_pop = df_neg['Popcorn (grams)'].std()
neg_std_soda = df_neg['Soda Pop (ml)'].std()
neg_std_candy = df_neg['Candy (grams)'].std()

print("The mean of the positive popcorn data is: {0}\n".format(pos_mean_pop))
print("The mean of the positive soda data is: {0}\n".format(pos_mean_soda))
print("The mean of the positive candy data is: {0}\n".format(pos_mean_candy))

print("The stardard deviation of the positive popcorn data is: {0}\n".format(pos_std_pop))
print("The stardard deviation of the positive soda data is: {0}\n".format(pos_std_soda))
print("The stardard deviation of the positive candy data is: {0}\n".format(pos_std_candy))


print("The mean of the negative popcorn data is: {0}\n".format(neg_mean_pop))
print("The mean of the negative soda data is: {0}\n".format(neg_mean_soda))
print("The mean of the negative candy data is: {0}\n".format(neg_mean_candy))

print("The stardard deviation of the negative popcorn data is: {0}\n".format(neg_std_pop))
print("The stardard deviation of the negative soda data is: {0}\n".format(neg_std_soda))
print("The stardard deviation of the negative candy data is: {0}\n".format(neg_std_candy))


#Calculate Prior Probability
pos_prior = df_pos.shape[0]/total_people
neg_prior = df_neg.shape[0]/total_people

print("The positive prior probability is: {0}\n".format(pos_prior))
print("The negative prior probability is: {0}\n".format(neg_prior))
print()
print((1/(m.sqrt(2*np.pi*(1.5)**2))) * np.exp(-((50-50)**2)/2*((1.5)**2)))
print()
#Calculate Likelihoods for new data for both positive and negative
pos_pop_likelihood = (1/(m.sqrt(2*np.pi*(pos_std_pop)**2))) * np.exp(-((new_data_to_classify[0]-pos_mean_pop)**2)/(2*((pos_std_pop)**2)))
pos_soda_likelihood = (1/(m.sqrt(2*np.pi*(pos_std_soda)**2))) * np.exp(-((new_data_to_classify[1]-pos_mean_soda)**2)/(2*((pos_std_soda)**2)))
pos_candy_likelihood = (1/(m.sqrt(2*np.pi*(pos_std_candy)**2))) * np.exp(-((new_data_to_classify[2]-pos_mean_candy)**2)/(2*((pos_std_candy)**2)))

neg_pop_likelihood = (1/(m.sqrt(2*np.pi*(neg_std_pop)**2))) * np.exp(-((new_data_to_classify[0]-neg_mean_pop)**2)/(2*((neg_std_pop)**2)))
neg_soda_likelihood = (1/(m.sqrt(2*np.pi*(neg_std_soda)**2))) * np.exp(-((new_data_to_classify[1]-neg_mean_soda)**2)/(2*((neg_std_soda)**2)))
neg_candy_likelihood = (1/(m.sqrt(2*np.pi*(neg_std_candy)**2))) * np.exp(-((new_data_to_classify[2]-neg_mean_candy)**2)/(2*((neg_std_candy)**2)))

print("The likelihood for positive popcorn is: {0}\n".format(pos_pop_likelihood))
print("The likelihood for positive soda is: {0}\n".format(pos_soda_likelihood))
print("The likelihood for positive candy is: {0}\n".format(pos_candy_likelihood))

print("The likelihood for negative popcorn is: {0}\n".format(neg_pop_likelihood))
print("The likelihood for negative soda is: {0}\n".format(neg_soda_likelihood))
print("The likelihood for negative candy is: {0}\n".format(neg_candy_likelihood))


#Calculate Scores - Use logs to prevent underflow
score_for_positive = np.log(pos_prior) + np.log(pos_pop_likelihood) + np.log(pos_soda_likelihood) + np.log(pos_candy_likelihood)
score_for_negative = np.log(neg_prior) + np.log(neg_pop_likelihood) + np.log(neg_soda_likelihood) + np.log(neg_candy_likelihood)

print("The score for positive is {0}".format(score_for_positive))
print("The score for negative is {0}".format(score_for_negative))

if score_for_positive > score_for_negative:
    print("Since the positive score is more than the negative score, the new data will be classified as positive")
else:
    print("Since the negative score is more than the positive score, the new data will be classified as negative")

