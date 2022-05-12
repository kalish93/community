def checkArithmeticSubarrays(nums, l, r):
    output = []
    for i in range(len(l)):
        temp = nums[l[i]:r[i]]
        temp.sort()
        # print(temp)
        
        if len(temp) > 1:
            difference = temp[1]-temp[0]
            temp.pop(0)
            # temp.pop(1)
            for i in range(len(temp)-1):
                if (temp[i+1] - temp[i])!= difference:
                    output.append(False)
                    break
                
                
                output.append(True)
                break
        else:
            output.append(True)
    # # return output
    print(output)
# nums = [4,6,5,9,3,7]
# l = [0,0,2]
# r = [2,3,5]
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
checkArithmeticSubarrays(nums, l, r)      
# print(checkArithmeticSubarrays(nums, l, r))