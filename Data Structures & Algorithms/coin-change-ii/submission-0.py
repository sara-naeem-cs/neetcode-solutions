class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        totalCombos = 0
        
        def dfs(remaining, startIndex):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            total = 0
            for i in range(startIndex, len(coins)):
                total += dfs(remaining - coins[i], i)  # what startIndex do you pass to keep going?
            return total

        return dfs(amount, 0)




