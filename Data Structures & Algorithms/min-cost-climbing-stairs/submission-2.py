class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(floorNum):
            if floorNum >= len(cost):
                return 0

            #for each floor we store what the cost will be from top-down
            #total at this floor + min of next two steps
            if floorNum in cache:
                return cache[floorNum]
            else: #floorNum not in cache
                cache[floorNum] = cost[floorNum] + min(dfs(floorNum + 1), dfs(floorNum + 2))
            return cache[floorNum]

        return min(dfs(0), dfs(1))
