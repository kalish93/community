class Solution:
    def kthLargestNumber(self, nums, k: int) :
        l = []
        for i in range(len(nums)):
            l.append(int(nums[i]))
        l.sort()
        return str(l[len(l)-k])