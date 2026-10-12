def isPalindrome(s):
    return s == s[::-1]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = [] #This holds our partition
        
        def dfs(startIndex):
            if startIndex >= len(s):
                res.append(part.copy())
                return
            
            for i in range(startIndex, len(s)):
                piece = s[startIndex:i+1]
                if isPalindrome(piece):
                    part.append(piece)
                    dfs(i+1)
                    part.pop()

        
        dfs(0)
        return res