nums=[1,2,3,4,5,6,7]
nums=[-1,-100,3,99]
k=2
# first methon
while k!=0:
    item=nums.pop(len(nums)-1)
    nums.insert(0,item)
    k-=1
print(nums)


# k=3
# seccond method
while k!=0:
    temp=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[len(nums)-1]=temp
    k-=1
print(nums)

        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # n = len(nums)
        # if k >= n:
        #     k  = k%n
        # def reverse(nums,s,e):
        #     while s < e:
        #         nums[s], nums[e] = nums[e], nums[s]
        #         s, e = s+1,e-1
        # reverse(nums,0, n-1)
        # reverse(nums,0, k-1)
        # reverse(nums,k ,n-1)
        # return nums



        # # return nums[k:] + nums[:k]

        # def reverse(arr,l,r):
        #     while l < r:
        #         arr[i], arr[j] = arr[j], arr[i]
        #         l += 1
        #         r -= 1
        #     return arr
        # n = len(nums)
        # reverse(nums,0,k)
        # print(nums)
        # reverse(nums,k,n)
        # print(nums)
        # reverse(nums,0,n)

        # return nums

        
            





















        
        