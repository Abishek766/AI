import numpy as num

random_integer=num.random.randint(1,51, size=(5,5))
print("Orignal : \n",random_integer)

random_integer[random_integer > 25]=0
print("Modified: \n",random_integer)

print("Sum: \n",num.sum(random_integer))
print("Mean: \n",num.mean(random_integer))
print("Standard Deivation: \n",num.std(random_integer))