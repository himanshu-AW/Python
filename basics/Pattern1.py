# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 
n=int(input("Enter number : ")) 
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(j,end=" ")
    for j in range(1,2*i):
        print(i,end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()
for i in range(2,n+1):
    for j in range(n,i,-1):
        print(j,end=" ")
    for j in range(1,2*i):
        print(i,end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()