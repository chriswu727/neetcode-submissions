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
        toco = { None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            toco[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = toco[cur]
            copy.next = toco[cur.next]
            copy.random = toco[cur.random]
            cur = cur.next
        return toco[head]