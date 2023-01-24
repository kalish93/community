# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        unsorted = []
        while current:
            unsorted.append(current.val)
            current = current.next         
        print(unsorted)
        unsorted.sort()
        current = head
        i = 0
        while current and i < len(unsorted):
            current.val = unsorted[i]
            current =current.next
            i+=1
        return head