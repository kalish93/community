class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 4 or n == 1:
            return True
        else:
            n = n/4
            return self.isPowerOfFour(n)
        return False
        