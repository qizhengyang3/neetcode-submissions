"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head

        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next

        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        newHead = cur.next

        while cur:
            newNode = cur.next
            cur.next = newNode.next
            newNode.next = newNode.next.next if newNode.next else None
            cur = cur.next

        return newHead



        

            
