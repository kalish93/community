class Solution:
    def rearrangeArray(self, nums):
        if len(nums) == 3:
            if ((nums[0] + nums[2])) / 2 == nums[1]:
                tem = nums.pop(1)
                nums.append(tem)
                
        else:
            for j in range(len(nums)):
                for i in range(len(nums)-1):
                    if ((nums[i-1] + nums[i+1])) / 2 == nums[i]:
                        temp = nums[i]
                        nums[i] = nums[i+1]
                        nums[i+1] = temp
        return nums

