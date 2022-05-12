

def isValid(s: str) -> bool:
    l = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            l.append(i)
        elif i == ')' and len(l) != 0:
            if l[-1] == '(':
                l.pop()
        elif i == ']' and len(l) != 0 :
            if l[-1] == '[':
                l.pop()
        elif i == '}' and len(l) != 0:
            if l[-1] == '{':
                l.pop()
        elif i == ')' and len(l) == 0:
            
            break
        elif i == ']' and len(l) == 0 :
            break
        elif i == '}' and len(l) == 0:
            break
        return False
            
        
    if len(l) == 0:
        return True
    # return False

s = '()'
print(isValid(s))