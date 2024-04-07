def smallestFromCurrentNum(nums):    
        temp = sorted(nums)
        length = len(nums)
        map = {}
        result = []
        for i in range(length):
            if temp[i] not in map:
                map[temp[i]] = i
        for j in range(length):
            result.append(map[nums[j]])
        return result

nums=[8,1,2,2,3]
print(smallestFromCurrentNum(nums))