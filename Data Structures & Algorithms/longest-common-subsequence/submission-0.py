class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            
            elif text1[i] == text2[j]:
                #We have a match so 
                return 1 + dfs(i+1, j+1)
            else:
                #The letters don't match so we want max of increment of i and j
                return max(dfs(i+1, j), dfs(i, j+1))
        

        return dfs(0, 0)