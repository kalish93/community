class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maxfreq = 0
        i,j = 0 , 0 
        total = 0
        nums.sort()
        while j < len(nums):
            total += nums[j]
            while total + k < nums[j] * ( j - i + 1):
                total -= nums[i]
                i+=1
            maxfreq = max(maxfreq, j - i + 1)
            j+=1
        return maxfreq
