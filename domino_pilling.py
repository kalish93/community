n, m = list(map(int, input().split()))
def dominoPilling(m,n):
    totalArea = m*n
    remainingArea = totalArea % 2
    totalTiles = (totalArea - remainingArea) / 2
    return totalTiles

print(dominoPilling(n,m))