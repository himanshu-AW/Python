nums=[1,2,25,50,75,90,95,105]
target=100
def twosum(nums,taget):
    i=0
    j=len(nums)-1
    while i<j:
        sum=nums[i]+nums[j]
        if sum==target:
            return [i+1,j+1]
        elif sum>taget:
            j-=1
        else:
            i+=1
    
print(twosum(nums,target))