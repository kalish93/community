
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = 0
        output = 0
        piles.sort()
        piles.reverse()
        print(piles)
        for i in range(1,len(piles),2):
            output += piles[i]
            n+=1
            if n == len(piles)//3:
                return output
        return output