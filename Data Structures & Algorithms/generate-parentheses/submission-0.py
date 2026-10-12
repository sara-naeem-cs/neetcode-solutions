class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def parentheses(currStr, openCount, closeCount):
            if openCount == n and closeCount == n:
                res.append(currStr)
                return
            
            if openCount == n or openCount > closeCount:
                parentheses(currStr+")", openCount, closeCount + 1)
            if openCount < n:
                parentheses(currStr+"(", openCount+1, closeCount)

            
        parentheses("", 0, 0)
        return res