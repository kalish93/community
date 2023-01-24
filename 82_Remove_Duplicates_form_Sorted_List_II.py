# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        print(prev)
        prev.next = head
        current = head
        
        while current and current.next:
            if current.val != current.next.val:
                prev = current
                current = current.next
            else: 
                while current.val == current.next.val:
                    current = current.next
                prev.next = current.next
                current = current.next
                
        return head