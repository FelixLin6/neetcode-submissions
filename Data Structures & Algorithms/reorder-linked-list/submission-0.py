# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        bank = []
        curr = head
        while curr:
            bank.append(curr)
            curr = curr.next
        n = len(bank)

        tail = ListNode()
        for i in range(n):
            if i % 2 == 0:
                tail.next = bank[i // 2]
            else:
                tail.next = bank[n - (i + 1) // 2]
            tail = tail.next

        tail.next = None