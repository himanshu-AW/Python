#Enter a number :5
#* * * * * * 
#*         *
#*         *
#*         *
#*         *
#* * * * * *
n=int(input('Enter a number :'))
for i in range(n+1):
    for j in range(n+1):
        if (i==0 or i==n):
            print('*',end=" ")
        elif( j==0 or j==n):
            print('*',end=" ") 
        else:
            print(' ',end=" ")
    print('\n',end="")   