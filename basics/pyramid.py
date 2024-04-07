n=int(input('enter a number :'))
i,j=1,1
for i in range(n+1):
    for j in range(n-i):
        print('-',end="")
    for j in range(2*i-1):
        print('*',end="")
    print('\n')