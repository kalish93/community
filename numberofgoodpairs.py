class Solution:
    def numIdenticalPairs(nums) -> int:
        nums.sort()
        ar = [0] * nums[-1]
        
        while len(nums) >0:
            temp = nums.pop(0)
            ar[temp-1] += 1
    

        output = 0
        for i in range(len(ar)):
            output += (ar[i] * (ar[i]-1) // 2) 
        return output