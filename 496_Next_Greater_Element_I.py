class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {i:j for j, i in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)
        for i in nums2:
            while stack and stack[-1] < i:
                temp = stack.pop()
                if temp in indices:
                    res[indices[temp]] = i
            stack.append(i)
        return res
