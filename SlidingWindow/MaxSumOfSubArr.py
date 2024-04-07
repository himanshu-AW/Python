arr=[8,5,6,4,3,9,7,1]
size=len(arr)-1
k=2

def Max(x,y):
    if(x>=y):
        return x
    else:
        return y

i,j,sum,max=0,0,0,0

while j<size:
    sum+=arr[j]
    if( j-i+1<k):
        j+=1
    elif (j-i+1==k):
        max=Max(max,sum)
        sum=sum-arr[i]
        i+=1
        j+=1

print(max)


