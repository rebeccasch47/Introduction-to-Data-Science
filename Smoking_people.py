import numpy as np

#Number of people
n_people = 1000

#Probability of smoking 
p_smoking = 0.2

#Generate random people with a 20% chance of smoking
random_people = np.random.choice([0,1], size=n_people, p=[1-p_smoking, p_smoking])

#Calculate the average number of smoking people 
average_smoking = np.mean(random_people)

#Calculate the total number of smoking people 
total_smoking = np.sum(random_people)

print("Random people array:", random_people)
print("Total number of smoking people:", total_smoking)
print("Average number of smoking people:", average_smoking)