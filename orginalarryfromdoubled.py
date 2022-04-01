def find(num):
    num.sort()
    o = []
    test = num[:]
    while len(num) > 2:
        temp = num.pop(0)
        for i in range(len(num)-1):
            if num[i] == 2 * temp:
                num.pop(i)
                o.append(temp)
                break
    if len(num) == 2:      
        if num[0] * 2 == num[1]:
            o.append(num[0])
    if len(o) == len(test)/2:
       return o
    else:
        return []
    
        

            
    
changed = [1,2,2,2,4,4]
print(find(changed))

