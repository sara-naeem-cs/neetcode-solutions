"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToClone = {}
        if not node:
            return None

        def dfs(node):
            #if it's already in oldToClone, exit
            if node in oldToClone:
                return oldToClone[node] #Return the cloned node we created

            #Alternatively, create clone
            clone = Node(node.val)
            #Add to our mapping:
            oldToClone[node] = clone

            #for each neighbor in the original we need to add it to the clone
            for neighbor in node.neighbors:
                #Our clone appends the CLONE neighbors
                clone.neighbors.append(dfs(neighbor)) 
            #return our clone node
            return clone
        
        return dfs(node)


            

        