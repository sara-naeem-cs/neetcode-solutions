class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        stored_paths = {}
        
        def dfs(i, j):
            if i >= m or j >= n or i<0 or j<0:
                return 0
            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in stored_paths:
                return stored_paths[(i,j)]
            
            stored_paths[(i,j)] = dfs(i+1, j) + dfs(i, j+1)


            return stored_paths[(i,j)]
        return dfs(0,0)