class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(index):
            if index == len(s):
                return 1
            
            #string starts with zero
            if s[index] == "0": 
                return 0 
            
            #Have we seen this index before? Bc then we can return from dp
            if index in dp:
                return dp[index]
            
            res = dfs(index+1)

            if (index + 1) < len(s) and (s[index] == "1" or (s[index] == "2" and s[index+1] in "123456")):
                res = res + dfs(index+2)
            dp[index] = res
            return res
        
        return dfs(0)


        