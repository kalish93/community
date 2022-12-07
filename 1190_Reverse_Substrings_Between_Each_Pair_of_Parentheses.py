class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = ''
        for i in s:
            if i == '(':
                stack.append(temp)
                temp = ''
            elif i == ')':
                temp = stack.pop() + "".join(reversed(temp))
            else:
                temp += i
        return temp