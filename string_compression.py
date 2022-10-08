class Solution:
    def compress(chars) -> int:
        i = 0
        j = 0
        while(i<len(chars)):
            chars[j] = chars[i]
            count = 1
            while (i + 1<len(chars) and chars[i] == chars[i+1]):
                i+=1
                count+=1
            if(count>1):
                for c in str(count):
                    chars[j+1]=c
                    j+=1
            i+=1
            j+=1
        return j

