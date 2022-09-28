class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i = 0
        for element in pushed:
            stack.append(element)
            while(len(stack) !=0 and i < len(popped) and stack[-1]==popped[i]):
                stack.pop()
                i+=1
        return len(stack) == 0