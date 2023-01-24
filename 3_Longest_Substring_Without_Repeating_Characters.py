class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxi = 0
        track = []
        while(i < len(s)):
            c = s[i]
            while c in track:
                track.pop(0)
                j +=1
            track.append(c)
            i +=1
           
            maxi = max(maxi,i-j)
            
                
        return maxi