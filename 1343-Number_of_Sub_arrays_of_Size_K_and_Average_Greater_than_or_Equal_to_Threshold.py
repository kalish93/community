class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        ans = 0
        i = 0
        j = k
        
        total = sum(arr[i:j])
        if total / k >= threshold:
            ans +=1
        while j < len(arr):
            total = total + arr[j] - arr[i]
            if total / k >= threshold:
                ans +=1
            i+=1
            j+=1
        return ans