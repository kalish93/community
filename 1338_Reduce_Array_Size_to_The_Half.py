from collections import Counter 


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        values = list(count.values())
        values.sort()
        values = list(reversed(values))
        count = 0
        size = 0
        for value in values:
            if size >= len(arr)/2:
                break
            else:
                size += value
                count+=1
        return count
            