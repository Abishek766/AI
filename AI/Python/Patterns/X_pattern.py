# *- X pattern
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i == j or j == n-1-i):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# number-X Pattern
n=5
for i in range(0,n):
    for j in range(0,n):
        if(i == j):
            print(j+1,end="")
        elif(j == n-1-i):
            print(n-i,end="")
        else:
            print(" ",end="")
    print()