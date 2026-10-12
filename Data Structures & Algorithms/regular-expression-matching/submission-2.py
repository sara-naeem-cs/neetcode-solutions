class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}

        def dfs(i, j):
            if i >= len(s) and j>=len(p):
                return True
            if i<len(s) and j>=len(p):
                return False
            
            #Want to see if match is valid
            match = i < len(s) and (s[i]==p[j] or p[j] == ".")

            if (j+1) < len(p) and p[j+1] == "*":
                #We need to do recursive calls to deal with the star
                #One case without star, one case with star
                if (i,j) not in cache:
                    cache[(i,j)]= dfs(i, j+2) or (match and dfs(i+1, j))
                return cache[(i, j)]

            #If we don't have a star
            if match:
                if (i,j) not in cache:
                    cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]

            if (i,j) not in cache:
                cache[(i,j)] = False
            return cache[(i,j)]
        return dfs(0,0)



