# n=5
# for i in range(0,n):
#     for j in range(i+1):
#         print(i+1,end=' ')
#     print()
# # Output
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print()
#Output
# 1     
# 1 2     
# 1 2 3     
# 1 2 3 4     
# 1 2 3 4 5

n=5
for i in range(0,n):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()
#Output
# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1