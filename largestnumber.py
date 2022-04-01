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
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    nums.sort(reverse=True)
    return nums
    
nums = [1,3,24,10]
print(largestNumber(nums))
///
# t = 78998
# t = list(str(t))
# print(t)