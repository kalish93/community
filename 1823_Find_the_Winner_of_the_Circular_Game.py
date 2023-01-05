class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]
    
        def findwinner(index, arr):
            if len(arr) == 1:
                return arr[0]
            else:
                arr.pop(index)
                return findwinner((index + k -1 ) % len(arr),arr)
    
        return findwinner((0 + k -1 ) % n,friends)