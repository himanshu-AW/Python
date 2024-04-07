# arr=[1,22,34,45,56,67,78,89,90]
arr=[23,34,56,67,78,3234,32,13,0,377,96,]
arr.sort()

# def binarySearch(arr,target):
#     l=0
#     s=len(arr)-1
#     while l<=s:
#         mid=(l+s)//2
#         if(target==arr[mid]):
#             return mid
#         elif(target<arr[mid]):
#             s=mid-1
#             binarySearch()
#         else:
#             l=mid-1
#     return -1

# recursive function
def binarySearch(arr,i,j,target):
    if(i>=j):
        return -1
    mid=(i+j)//2
    if(target==arr[mid]):
        return mid
    elif (target<arr[mid]):
        binarySearch(arr,i,mid-1,target)
    else:
        binarySearch(arr,mid+1,j,target)


if(binarySearch(arr,0,len(arr)-1,56)!= -1):
    print(f"{56} Found at index {binarySearch(arr,0,len(arr)-1,56)}")
else:
    print(f"{56} not Found !")