class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0: return "0"
        strnums = [str(num) for num in nums]
        
        for i in range(len(strnums)):
            j = i+1
            for j in range(len(strnums)-1):
                if strnums[j] + strnums[i] < strnums[i] + strnums[j]:
                    strnums[j] , strnums[i] = strnums[i] , strnums[j]
        return "".join(map(str,strnums))