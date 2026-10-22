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
        # Hash: {original node: copy node}
        nodes = {}


        # Iterating we create copy of the nodes and store them in hashmap
        cur = head

        if not head:
            return None
            
        while cur:
            temp = Node(cur.val)
            nodes[cur] = temp
            cur = cur.next

        #Then iterate again, and assign the pointers
        cur = head
        while cur:
            nodes[cur].next = nodes[cur.next] if cur.next else None
            if cur.random:
                nodes[cur].random = nodes[cur.random]
            else:
                nodes[cur].random = None

            cur = cur.next
                
        return nodes[head]

