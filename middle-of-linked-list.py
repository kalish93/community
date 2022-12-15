# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # j=head
        # i=head
        # while(j and j.next):
        #     j = j.next.next
        #     i = i.next
        # return i

        temp=middlenode = head
        count = 0
        while(temp):
            temp=temp.next
            count +=1
        middle = count//2
        middlecount = 0
        while(middlenode):
            if middlecount == middle:
                return middlenode
            else:
                middlecount+=1
                middlenode = middlenode.next