"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        h = {}
        h[node] = Node(node.val)
        q = [node]

        while q:
            c = q.pop()
            for i in c.neighbors:
                if i not in h:
                    new_node = Node(i.val)
                    h[i] = new_node
                    q.append(i)
                h[c].neighbors.append(h[i])
        
        return h[node]
