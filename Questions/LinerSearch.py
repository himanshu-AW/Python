arr=[23,34,56,67,78,3234,32,13,0,377,96,]

def linerSearch(arr,target):
    count=0
    i=0
    while i<len(arr):
        if(arr[i]==target):
            return i , count
        count+=1
        i+=1
    return "Not Found" , count

print(linerSearch(arr,67))     
print(linerSearch(arr,87))     
