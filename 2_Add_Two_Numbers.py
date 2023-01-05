# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current = l1
        nums1 =[]
        while current:
            nums1.append(str(current.val))
            current = current.next
        nums1.reverse()
        num1 = "".join(nums1)
        num1 = int(num1)
        current = l2
        nums2 = []
        while current:
            nums2.append(str(current.val))
            current = current.next
         
        nums2.reverse()
        num2 = "".join(nums2)
        num2 = int(num2)
        
        num = num1 + num2
        num = str(num)
        nums = list(num)
        
        intnums = [int(i) for i in nums]
        
        for i, digit in enumerate(intnums):
            if i == 0:
                intnums[i] = ListNode(val = digit, next=None)
            else: 
                intnums[i] = ListNode(val = digit, next=intnums[i-1])
        return intnums[len(intnums)-1]