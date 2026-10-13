class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy --> i + 1
        #sell --> i + 2

        def dfs(i, day):
            if i >= len(prices):
                return 0
            
            #Either option has a cooldown day
            cooldown_amt = dfs(i + 1, "buy") #price stays the same

            #if the day is buy we can sell 
            if day == "buy":
                #We can sell
                buy_amt = dfs(i+1, "sell") - prices[i]
                return max(buy_amt, cooldown_amt)
            else:
                #If the day is sell, we can buy
                sell_amt = dfs(i+2, "buy") + prices[i]
                return max(sell_amt, cooldown_amt)
            
        return dfs(0, "buy")

                

            