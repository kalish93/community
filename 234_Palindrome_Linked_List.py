# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        current = head
        while current:
            temp.append(current.val)
            current = current.next
        while len(temp) >0:    
            if temp[0] == temp[-1]:
                temp = temp[1:-1]
                # print(temp)
            else:
                return False
        return True