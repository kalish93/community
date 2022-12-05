class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        output = []
        for i in range(len(l)):
            temp = nums[l[i]:(r[i]+1)]
            print(temp)
            temp.sort()
            difference = {abs(temp[i +1] - temp[i]) for i in range(len(temp)-1)}
            if len(difference) == 1:
                output.append(True)
            else:
                output.append(False)
        return output