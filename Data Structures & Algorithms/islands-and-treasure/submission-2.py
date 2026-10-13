class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def dfs(i, j, pathLen, visited):
            if i < 0 or i >= len(grid) or j < 0 or j>=len(grid[0]):
                return float("inf")
            if grid[i][j] == -1:
                return float("inf")
            if grid[i][j] != -1 and grid[i][j]!=0 and grid[i][j] != 2147483647 :
                return pathLen + grid[i][j]
            if grid[i][j]==0:
                return pathLen

            if (i,j) in visited:
                return float("inf")
            else:
                visited.add((i,j))

            
            return min(dfs(i+1, j, pathLen+1, visited), dfs(i-1, j,pathLen+1, visited), dfs(i, j+1,pathLen+1, visited), dfs(i, j-1,pathLen+1, visited))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    #Find value of the shortest path. 
                    visited = set()
                    grid[i][j] = dfs(i, j, 0,visited)

                    if grid[i][j] == float("inf"):
                        grid[i][j] = 2147483647

