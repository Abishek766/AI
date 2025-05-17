n=5
for i in range(0,n):
    for k in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("* ",end=" ")
    print()
for i in range(0,n):
    for k in range(0,i):
        print(" ",end=" ")
    for j in range(0,n-i):
        print("* ",end=" ")
    print()