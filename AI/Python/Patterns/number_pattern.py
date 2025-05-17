# n =5
# count=0
# for i in range(0,n):
#     for j in range(0,n):
#         count+=1
#         if(count <10):
#           print(0,end="")
#         print(count,end=" ")
#     print()
# #Output
# 01 02 03 04 05 
# 06 07 08 09 10 
# 11 12 13 14 15 
# 16 17 18 19 20 
# 21 22 23 24 25

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i * j < 10):
#             print(0,end="")
#         print(i*j,end=" ")
#     print()
#Output
# 01 02 03 04 05 
# 02 04 06 08 10 
# 03 06 09 12 15 
# 04 08 12 16 20 
# 05 10 15 20 25 

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()
#Output
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()
# Output
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 

n=5
count=0
for i in range(0,n):
    count=i+1
    for j in range(0,n):
        print(count,end=" ")
        count+=1
    print()