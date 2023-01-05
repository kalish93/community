class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            inverted = ""
            for i in s:
                if i == '0':
                    inverted += '1'
                else:
                    inverted += '0'
            return inverted
        def recurse(n):
            if n == 0:
                return "0"
            s = recurse(n-1)
            return s + "1" + invert(s)[::-1]
            
        x = recurse(n)
        return x[k-1]