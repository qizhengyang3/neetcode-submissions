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
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next

            cur = cur.next.next

        cur = head
        new_head = cur.next

        while cur:
            new_node = cur.next
            cur.next =  new_node.next
            new_node.next = new_node.next.next if new_node.next else None
            cur = cur.next

        return new_head
            