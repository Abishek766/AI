from itertools import product
import numpy as np

#Set sample of a rolling dice
sample_space = list(range(1,7))

#Probability of rolling an even number
even_number = [2,4,6]
P_even = len(even_number)/len(sample_space)
print("Probability of even number: ",P_even)

# Random variable : dice roll
outcomes = np.array([1,2,3,4,5,6])
probability = np.array([1/6]*6)

#Expectation
expectation = np.sum(outcomes * probability)
print("Expectation (Mean): ", expectation)

#Varience and Standard deviation
varience = np.sum((outcomes - expectation)**2 * probability)
sta_dev = np.sqrt(varience)

print("Varience: ",varience)
print("Standard Deviation: ",sta_dev)
