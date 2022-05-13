def topKFrequent(nums,k):
    nums.sort()
    top = nums[-1]
    count = [0]* (top+1)
    output = []
    for i in nums:
        count[i] +=1
    for i in range(k):
        largest = count.index(max(count))
        print(count)
        print(largest)
        output.append(largest)
        count[largest] = 0
        print(count)
    return output
nums = [-1,-2]
print(topKFrequent(nums,3))