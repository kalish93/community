class Solution:
    def pivotIndex(self, nums) -> int:
        total = sum(nums)
        left = 0
        x = 0
        while(x<len(nums)):
            if(left == total - nums[x] - left):
                return x
            left += nums[x]
            x+=1
        return -1