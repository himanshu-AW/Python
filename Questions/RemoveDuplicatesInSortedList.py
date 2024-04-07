
nums=[1,1,2,3,3,3]
# def removeDuplicates( nums):
#         curr=-1
#         for i in nums:
#             if(curr==-1):
#                 curr=i
#             elif curr==i:
#                 nums.remove(i)
#             else:
#                 curr=i
#         return nums

# print(removeDuplicates(nums))

def removeDuplicates( nums):
        s=set()
        c=0
        for i in range(0,len(nums)-c):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                nums.remove(nums[i])
                c+=1
        return nums
                

print(removeDuplicates(nums))