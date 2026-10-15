class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = []
        #n nodes and n edges
        #Set each node as it's own parent
        for i in range(len(edges)+1):
            parents.append(i)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            else:
                parents[ra] = rb
                return True



        for edge in edges:
            cycle = union(edge[0], edge[1])
            if not cycle:
                return edge
        
        return 0

        