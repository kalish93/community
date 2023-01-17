# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        current = head
        while current:
            size+=1
            current = current.next
        counter = size - n 
        if size == 1:
            head = None
            return head
        if size == n:
            head = head.next
            return head
        current = head
        for i in range(counter-1):
            current = current.next
        current.next = current.next.next
        return head