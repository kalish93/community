# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            j = head
            while j != current:
                if j.val > current.val:
                    j.val , current.val = current.val, j.val
                j = j.next
            current = current.next
        return head
            
            
            