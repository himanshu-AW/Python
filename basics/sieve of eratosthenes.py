#Sieve Of Eratosthenes
def SieveOfEratosthenes(n):
    prime=[True for i in range(n+1)]
    #print(prime)
    p=2
    while(p*p <= n):
        # if it remain unchange it is prime
        if (prime[p]==True):
            #updating all the multiples
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    prime[0],prime[1]=False,False
    #display /Print
    for p in range(n+1):
        if prime[p]:
            print (p,end=', ')
    
if __name__=='__main__':
    n=33
    print('The prime NUmbers smaller than or equal to  ',n,'is')
    SieveOfEratosthenes(n)