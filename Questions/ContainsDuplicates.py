nums=[1,2,3,1]
def chekDup(nums):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]== nums[j]:
                return True
    return False
    

def chekDup2(nums):
    s=set(nums)
    for x in nums:
        if x in s:
            return True ,x
    return False



print(chekDup2(nums))