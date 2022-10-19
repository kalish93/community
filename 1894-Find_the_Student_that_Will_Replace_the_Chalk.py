class Solution:
    def chalkReplacer(self, chalk, k: int) -> int:
        k %= sum(chalk)
                     
        for i in range(len(chalk)):
            if k - chalk[i] < 0:
                return i
            else:
                k -= chalk[i]