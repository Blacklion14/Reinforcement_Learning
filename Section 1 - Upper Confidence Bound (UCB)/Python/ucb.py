#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the data set
dataset = pd.read_csv('Ads_CTR_Optimisation.csv') 

#Implimenting UCB
import math 
N = 10000
d = 10
ads_selected = []
no_of_selecion = [0] * d
sum_of_reward = [0] * d
total_reward = 0
for n in range(0 , N):
    ad = 0
    max_upper_bound = 0
    for i in range(0 , d):
        if (no_of_selecion[i] > 0):
            average_reward = sum_of_reward[i] / no_of_selecion[i]
            delta_i = math.sqrt((3/2) * (math.log(n+1)/no_of_selecion[i]))
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    no_of_selecion[ad] += 1
    reward = dataset.values[n , ad]
    sum_of_reward[ad] += reward 
    total_reward += reward        
    
#Visualizing the results
plt.hist(ads_selected)
plt.title('Histogram')
plt.xlabel('Ads')
plt.ylabel('No of time each ad was selected')
plt.show()    
    