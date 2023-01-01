

nums = [2,3,2,3,8,1]

print(nums[0:2])

def shortestSubarray(nums, k: int) -> int:
    i = 0
    j = 0
    subarray = []
    while i < len(nums) and j+1 < len(nums):
        if sum(nums[i:j]) < k:
            j += 1
        if sum(nums[i:j]) >= k:
            subarray.append(j - i)
            i +=1
            j +=1
            print(i,j)
            
    if len(subarray) == 0:
        return -1
    print(subarray)
    return min(subarray)


print(shortestSubarray(nums,8))