from statistics import mode
from collections import Counter

import scipy.stats as stats

data = [10,20,30,40,50]
mean = sum(data)/len(data)


# print(f"Mean is {mean}")

# sorted_data = sorted(data)
# median = sorted_data[len(data)//2] if len(data) %2 !=0 else \
#      (sorted_data[len(data)//2-1] + sorted_data[len(data)// 2])/2
# print(f"Median is {median}")

# mode_result = mode(data)
# print("Mode: ",mode_result) # Note: In statistics and scipy library if there is no mode in a data set it will return smallest value in a date set as a default behaivor

# #To overcome or get a coorect solution we use Collection.counter

# counts = Counter(data)
# max_freq = max(counts.values())

# modes=[k for k, v in counts.items() if v == max_freq]

# if len(modes) == len(data): # all output have 1 frequency
#     print("No modes")
# else:
#     print("Mode(s) ",modes)

variance = sum((x - mean) **2 for x in data)/len(data)
std_dev = variance **0.5

sample_mean= mean
z_score = 1.96
CI = (sample_mean - z_score *(std_dev/ len(data)),sample_mean + z_score *(std_dev/ len(data)))
print("95% Confidence Interval: ",CI)