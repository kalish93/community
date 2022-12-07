
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        if k == len(nums):
            return nums
        return [x[0] for x in count.most_common(k)]
        

