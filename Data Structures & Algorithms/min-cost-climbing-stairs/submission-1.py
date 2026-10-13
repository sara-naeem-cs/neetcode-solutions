class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(currTotal, floorNum):
            if floorNum >= len(cost):
                return currTotal

            return min(
                dfs(currTotal + cost[floorNum], floorNum + 1),
                dfs(currTotal + cost[floorNum], floorNum + 2),
            )

        return min(dfs(0, 0), dfs(0, 1))
