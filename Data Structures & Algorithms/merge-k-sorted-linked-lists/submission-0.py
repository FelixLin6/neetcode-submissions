# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flattened = []
        for lst in lists:
            curr = lst
            while curr:
                flattened.append(curr.val)
                curr = curr.next
        
        head = curr = ListNode()
        for n in sorted(flattened):
            curr.next = ListNode(n)
            curr = curr.next
        
        return head.next