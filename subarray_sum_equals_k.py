class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count=0
        prefsum =0
        d={}
        for num in nums:
            prefsum = prefsum + num
            if prefsum == k:
                count +=1
            if prefsum-k in d:
                count = count + d[prefsum-k]
                
            if prefsum in d:
                d[prefsum] = d[prefsum]+1
                
            else:
                d[prefsum] = 1
        return count