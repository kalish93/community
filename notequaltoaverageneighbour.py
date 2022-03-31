def rearrangeArray(nums):
    
    # if len(nums) == 3:
    #     nums.sort()
    #     temp = nums.pop(1)
    #     nums.append(temp)
    #     return nums
    # nums.sort()
    # if len(nums) > 3:
        
    #     if len(nums) % 2 == 0:
    #         tem = nums.pop(len(nums)//2 -1)
    #     else:
    #         tem = nums.pop(len(nums)//2)
    #     for i in range(len(nums)-2):
    #         temp = nums[i]
    #         nums[i] = nums[i+2]
    #         nums[i+2] = temp
    #     nums.append(tem)
    #     return nums
    # tem = nums.pop(len(nums)//2)
    for j in range(len(nums)):
        for i in range(len(nums)-1):
            if ((nums[i-1] + nums[i+1])) / 2 == nums[i]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        # nums.append(tem)
    return nums
l = [0,4,5,3,1]

print(rearrangeArray(l))