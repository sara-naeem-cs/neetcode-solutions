class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        subseqs = {}
        
        def dfs(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            
            if text1[i] == text2[j]:
                if (i,j) not in subseqs:
                    subseqs[(i,j)] = 1 + dfs(i+1, j+1)
                #We have a match so 
                return subseqs[(i,j)]
            else:
                if (i,j) not in subseqs:
                    subseqs[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
                #The letters don't match so we want max of increment of i and j
                return subseqs[(i,j)]
        

        return dfs(0, 0)