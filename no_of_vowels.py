class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        maxi = 0
        count = 0
        vowles = ["a","e","i","o","u"]
        while(i<len(s)):
            if s[i] in vowles:
                count+=1
            if i < k-1:
                i+=1
            elif (i - j + 1) == k:
                maxi = max(maxi, count)
                if s[j] in vowles:
                    count-=1
                j+=1
                i+=1
                
        return maxi