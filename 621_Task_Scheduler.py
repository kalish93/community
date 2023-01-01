from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxcount = 0
        maxvalue = max(count.values())
        counts = list(count.values())
        for value in counts:
            if value == maxvalue:
                maxcount += 1
        return max((n+1)*(maxvalue - 1) + maxcount, len(tasks))