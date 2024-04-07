# s=str()
# for i in digit:
#     s+=str(i)
# a=int(s)
# a+=1
# s=str(a)
# l=list(s)
# print(l)
# print(type(l))

def PlusByOne(digit):
    n=len(digit)-1
    while n>=0:
        temp=digit[n]+1
        if temp>9:
            digit[n]=0
            n-=1
        else:
            digit[n]=temp
            break
    
    if n==-1:
        digit.insert(0,1)
    return digit

digit=[9]
print(PlusByOne(digit))