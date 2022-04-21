from tkinter import N


def largestNumber(nums):
    # for i in range(len(nums)):
   
#     print(nums)
#     a = []
#     b = []
#     for i in range(len(nums)):
#         temp = nums.pop()
#         if temp > 10:
#             a.append(temp)
#         else:
#             b.append(temp)
#     output = ''
#     for i in a:
#         b.append(i)
#     b.sort(reverse=True)
#     for i in range(len(b)):
#         output += str(b[i])
#     return output
    # for i in range(len(nums)):
    #     nums[i] = str(nums[i])
    # nums.sort(reverse=True)
    # return nums
    nums.sort()
    a = []
    for i in range(len(nums)-1):
        if nums[i] == 10:
            temp = nums.pop(i)
            a.append(temp)
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    
    nums.sort(reverse=True)
    print(nums)
    output = ''
    for i in nums:
        output += str(i)
    for i in a:
        output += str(i)
    return output

    
nums = [33,30,34,5,9]
nums.sort()
print(nums)
print(largestNumber(nums))
# t = 78998
# t = list(str(t))
# print(t)