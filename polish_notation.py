class Solution:
    def evalRPN(self, tokens) -> int:
        tempList = []
        while(len(tokens)>0):
            temp = tokens.pop(0)
            if ((temp == '+') or (temp == '/') or (temp == '*') or (temp == '-')):

                num1 = tempList.pop()
                num2 = tempList.pop()
                if temp == '+':
                    result = num2 + num1
                elif temp == '-':
                    result = num2 - num1
                elif temp == '*':
                    result = num2 * num1
                elif temp == '/':
                    result = int(num2/num1)
                tempList.append(result)

            else:
                tempList.append(int(temp))
        return tempList.pop()




