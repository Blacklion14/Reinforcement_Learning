#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the data set
dataset = pd.read_csv('Ads_CTR_Optimisation.csv') 

#Implimenting Thompsan Sampling
import random 
N = 10000
d = 10
ads_selected = []
no_of_reward_1 = [0] * d
no_of_reward_0 = [0] * d
total_reward = 0
for n in range(0 , N):
    ad = 0
    max_random = 0
    for i in range(0 , d):
        random_beta = random.betavariate(no_of_reward_1[i] + 1, no_of_reward_0[i] + 1)
        if (random_beta > max_random):
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n , ad]
    if reward == 1:
        no_of_reward_1[ad] += 1
    else:    
        no_of_reward_0[ad] += 0
    total_reward += reward    

#Visualizing the results
plt.hist(ads_selected)
plt.title('Histogram')
plt.xlabel('Ads')
plt.ylabel('No of time each ad was selected')
plt.show()

        






