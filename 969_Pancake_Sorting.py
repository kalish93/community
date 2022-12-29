class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        if arr == sorted(arr):
            return []
        while len(arr) > 0:
            maxindex = arr.index(max(arr))
            output.append(maxindex + 1)
            temp = arr[:maxindex + 1] 
            temp = list(reversed(temp)) 
            arr = temp + arr[maxindex+1:]
            arr = list(reversed(arr))
            output.append(len(arr))
            arr.pop()
        return output
            