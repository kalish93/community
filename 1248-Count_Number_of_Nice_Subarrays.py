class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        d = {0:1}
        count = 0
        ans = 0
        for i, n in enumerate(nums):
            if n % 2 != 0:
                count += 1
            if count - k in d:
                ans += d[count - k]
            if count not in d:
                d[count] = 0
            d[count] += 1
        return ans