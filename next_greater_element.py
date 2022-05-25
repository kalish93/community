
def grea(nums1,nums2):
    output = []

    for i in range(len(nums1)-1):
        for j in range(len(nums2)-1):
            if nums1[i] == nums2[j]:
                if(nums2[-1] == nums2[j]):
                    output.append(-1)
                elif nums2[j] < nums2[j+1]:
                    output.append(nums2[j+1])
                output.append(-1)

    return output

n1 =[4,1,2]
n2 = [1,2,3,4]
print(grea(n1,n2))