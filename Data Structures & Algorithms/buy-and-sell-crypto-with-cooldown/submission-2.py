class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy --> i + 1
        #sell --> i + 2

        dp = {}

        def dfs(i, day):
            if i >= len(prices):
                return 0
            
            if (i, day) in dp:
                return dp[(i, day)]

            #Either option has a cooldown day
            cooldown_amt = dfs(i + 1, day) #price stays the same

            #if the day is buy we can sell 
            if day == "buy":
                #We can sell
                buy_amt = dfs(i+1, "sell") - prices[i]
                dp[(i, "buy")] = buy_amt
                return max(dp[(i, "buy")], cooldown_amt)
            else:
                #If the day is sell, we can buy
                sell_amt = dfs(i+2, "buy") + prices[i]
                dp[(i, "sell")] = sell_amt
                return max(dp[(i, "sell")], cooldown_amt)
            
        return dfs(0, "buy")

                

            