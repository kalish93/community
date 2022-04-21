# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reverse(s[:-1])

# print(reverse('sees'))

# def mergeSort(nums):
#     if len(nums) > 1:
#         first = nums[: len(nums)//2]
#         mergeSort(first)
#         second = nums[len(nums)//2:]
#         mergeSort(second)
#         merge(first,second,nums)
# def merge(first,second,nums):
#     temp = []
#     counter1 = 0
#     counter2 = 0
#     counter3 = 0
#     for i in range(len)

# print(mergeSort([1,2,3,4]))

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums.pop()
        left = []
        right = []
        for i in nums:
            if i > pivot:
                right.append(i)
            else:
                left.append(i)
    return quickSort(left) + [pivot] + quickSort(right)

nums = [22,11,88,66,55,77,33,44]
print(nums)
print(quickSort(nums))