class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))   # par[i] = i initially, each node is its own parent
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[res]   # path compression (halving)
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0   # already connected, no new merge happened
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1   # merge happened

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res