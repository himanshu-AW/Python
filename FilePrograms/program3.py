def computeGCD(x,y):
    if(x>y):
        small=y
    else:
        small=x

    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            gcd=i
    return gcd

n1=119
n2=21
print('the gcd of ',n1,'and',n2,'is :',computeGCD(n1,n2))
  