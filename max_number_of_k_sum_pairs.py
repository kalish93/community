
from collections import Counter
def maxOperations(nums, k):
    counter = Counter(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] == k/2:
            count+= (counter[nums[i]]//2)
            del counter[nums[i]]
        else:
            count += min(counter[nums[i]],counter[k-nums[i]])
            del counter[nums[i]]
            del counter[k-nums[i]]
        
    return count
nums = [3,1,3,4,3]
print(maxOperations(nums,4))