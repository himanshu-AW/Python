
for i in range(2,n+1):
    for j in range(n,i,-1):
        print(j,end=" ")
    for j in range(1,2*i):
        print(i,end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()