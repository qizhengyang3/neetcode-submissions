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

        left = head
        right = prev

        while right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            right.next = tmp1
            left = tmp1
            right = tmp2

