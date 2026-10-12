class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longestPaths = {}

        def dfs(row, column):
            if (row, column) in longestPaths:
                return longestPaths[(row, column)]

            # Otherwise, we need to find current longest path and store it.
            longestPath = 1

            if row + 1 < len(matrix) and matrix[row + 1][column] > matrix[row][column]:
                longestPath = max(longestPath, dfs(row + 1, column) + 1)
            if row - 1 >= 0 and matrix[row - 1][column] > matrix[row][column]:
                longestPath = max(longestPath, dfs(row - 1, column) + 1)
            if column + 1 < len(matrix[0]) and matrix[row][column + 1] > matrix[row][column]:
                longestPath = max(longestPath, dfs(row, column+1) + 1)
            if column - 1 >= 0 and matrix[row][column - 1] > matrix[row][column]:
                longestPath = max(longestPath, dfs(row, column-1) + 1)
            
            longestPaths[(row, column)] = longestPath

            return longestPaths[(row, column)]

        curr = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = max(curr, dfs(i,j))
        return curr
