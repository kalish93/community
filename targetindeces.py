class Solution:
    def targetIndices(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        output = []
        for j in range(len(nums)):
            if nums[j] == target:
                output.append(j)

        return output          
        # return nums