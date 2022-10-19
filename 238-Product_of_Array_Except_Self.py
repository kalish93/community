class Solution:
    def productExceptSelf(self, nums):
        outPut = []
        product = 1
        for i in range(len(nums)):
            product = product *nums[i]
            outPut.append(product)
        product = 1
        for i in range(len(nums)-1,0,-1):
            outPut[i] = product * outPut [i-1]
            product = product * nums[i]
        outPut[0] = product
        return outPut
        