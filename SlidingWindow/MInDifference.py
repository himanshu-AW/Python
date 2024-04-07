arr=[87063,61094,44530,21297,95857,93551,9918]
k=6
size=len(arr)-1
# arr.sort()
# print(arr)
min_diff=arr[k-1]-arr[0]

i=0
j=k-1
while j < size:
    min_diff=min(min_diff,arr[i]-arr[i-k+1])
    i+=1
    j+=1

print(min_diff)