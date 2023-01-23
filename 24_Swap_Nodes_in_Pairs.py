# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        output.next = head
        node = output
        
        while(node):
            first = node.next
            second = None
            if first:
                second = first.next
            if second:
                secondNext = second.next
                second.next = first
                node.next = second
                first.next = secondNext
                node = first
            else:
                break
        return output.next