#  by seive of Erathos Theorem
n=int(input('Enter a number :'))
prime=[]
l=list(range(1,n+1))
l.pop(0)
l.insert(0,0)
i=2
for i in l:
    if i!=0:
        prime.append(i)
        for j in range(i,n+1,i) :
            l.pop(j-1)
            l.insert(j-1,0)
            j=j+i
    else:
        continue
print(f"All Prime no is here in between {2} And {n} : {prime}")