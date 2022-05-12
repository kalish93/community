def max(nums):
    output = 0
    nums.sort()
    print(nums)
    nums.pop()
    for i in range(len(nums)-1,1,-3):
        print(nums[i])

nums = [2,4,1,2,7,8]
max(nums)