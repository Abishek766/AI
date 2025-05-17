import numpy as num

num.random.seed(3)
random_array=num.random.rand(3,3)
print("Random Array: \n",random_array)

random_integer=num.random.randint(0,10,size=(2,3))
print(random_integer)