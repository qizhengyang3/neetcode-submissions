# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        prev = slow.next = None
        cur = second

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        right = head
        left = prev

        while left:
            tmp1 = right.next
            tmp2 = left.next
            right.next = left
            left.next = tmp1
            right = tmp1
            left = tmp2

