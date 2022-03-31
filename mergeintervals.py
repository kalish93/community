def merge(intervals):
    intervals.sort()
    l = []
    
    if len(intervals) != 1:
        # print(intervals)
        temp = intervals.pop(0)
        # print(intervals)
        if temp[0] <= intervals[0][0] and temp[1] >= intervals[0][1]:
            temp = intervals[0]
            l.append(temp)
            intervals.pop(1)
        elif temp[0] <= intervals[0][0] and temp[1] >= intervals[0][0]:
            temp = [temp[0],intervals[0][1]] 
            temp = intervals[0]
            l.append(temp)
            intervals.pop(1)
        elif temp[0] >= intervals[0][0] and temp[1] <= intervals[0][0]:
            temp = [intervals[0][0],temp[1]] 
            temp = intervals[0]
            l.append(temp)
            intervals.pop(1)
        # else:
            # temp = intervals[0]
            # l.append(temp) 
    if len(intervals) == 1:
        l.append(intervals[0])
    return l    
intervals =  [[1,3],[2,6],[9,10]]
print(merge(intervals))