class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        i = 0
        j = len(nums)-1
        while i < j:
            maxSum = max(maxSum, nums[i] + nums[j])
            i+=1
            j-=1
        return maxSum

