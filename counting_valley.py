def countingValleys(steps, path):
    # Write your code here
    count = 0
    valley = 0
    path = list(path)
    for i in path:
        if i == 'U':
            count+=1
            if count == 0:
                valley+=1
        elif i == 'D':
            count-=1
            if count == 0:
                valley+=1
        # if count == 0:
        #     valley+=1
    return valley

path = 'UDDDUDUU'
print(countingValleys(len(path),path))



