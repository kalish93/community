# def find(num):
#     num.sort()
#     o = []
#     test = num[:]
#     while len(num) > 2:
#         temp = num.pop(0)
#         for i in range(len(num)-1):
#             if num[i] == 2 * temp:
#                 num.pop(i)
#                 o.append(temp)
#                 break
#     if len(num) == 2:      
#         if num[0] * 2 == num[1]:
#             o.append(num[0])
#     if len(o) == len(test)/2:
#        return o
#     else:
#         return []

from collections import Counter


class Solution:
    def findOriginalArray(self, nums):
        nums.sort()
        counts = Counter(nums)
        temp = []
        for num in nums:
            if counts[num] > 0:
                counts[num] -= 1
            else:
                continue
                
            double = num * 2
            if double in counts and counts[double] > 0:
                temp.append(num)
                counts[double] -=1
            
        if len(temp) == len(nums)/2:
            return temp
        return []
        