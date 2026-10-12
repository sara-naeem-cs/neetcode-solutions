class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(remaining, startIndex):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            total = 0
            for i in range(startIndex, len(coins)):
                if (remaining-coins[0], i) not in cache:
                    cache[(remaining-coins[0], i)] = dfs(remaining - coins[i], i)
                total += cache[(remaining-coins[0], i)]
            return total

        return dfs(amount, 0)




