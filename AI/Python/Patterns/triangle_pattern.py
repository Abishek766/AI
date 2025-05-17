# n=5
# for i in range(0,n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# Output
# * 
# * * 
# * * * 
# * * * *
# * * * * *

# Pyramid pattern
n=5
for i in range(0,n):
    for k in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("* ",end=" ")
    print(" ")

#mirror image of right angle triangle

