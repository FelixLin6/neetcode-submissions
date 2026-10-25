# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        m = l - n
        curr = head
        head = ListNode()
        head.next = curr
        prev = head
        for _ in range(m):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return head.next
