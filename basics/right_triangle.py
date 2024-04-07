n=5
for i in range(n):
    print('*'*(i+1))
for j in range(n):
    print('*'*(n-j-1))

    #neated loop
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
for i in range(1,n):
    for j in range(n-i):
        print('*',end='')
        j-=1
    print()

#another way
for i in range(1,n*2):
    if i<=5:
        for j in range(1,i+1):
            print('*',end='')
        print()
    else:
        for j in range(2*n-i):
            print('*',end='')
        print()
