class Solution:
    def kClosest(self, points, k: int):
        l = []
        for i in range(len(points)):
            temp = ((points[i][0]**2)+(points[i][1]**2))
            l.append(temp)
        print(l)
        for i in range(len(l)):
            for j in range(len(l)-1):
                if l[j] > l[j+1]:
                    temp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = temp
        list1 = l[0:k]
        print(list1)
        output = []
        for j in range(len(list1)):
            for i in range(len(points)):
                if ((points[i][0]**2)+(points[i][1]**2)) == list1[j]:
                    output.append(points[i])

        return output
