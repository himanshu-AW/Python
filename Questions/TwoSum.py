def twoSum( nums, target: int):
        for i,j in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]



nums=[2,0,3,5,7]
print(twoSum(nums,7))
