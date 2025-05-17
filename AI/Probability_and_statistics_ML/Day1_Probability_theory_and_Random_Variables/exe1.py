import numpy as np

#Simulating 10,000 dice rolls

dice = np.random.randint(1,7,10000)
# print(dice)

#Calculate Probabilites
p_even = np.sum(dice % 2 == 0)/len(dice)
p_greater = np.sum(dice > 4)/len(dice)

print("P (even): ",p_even)
print("p(greater than 4): ",p_greater)