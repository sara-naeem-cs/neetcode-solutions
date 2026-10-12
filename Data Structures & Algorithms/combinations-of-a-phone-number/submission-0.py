class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letDict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wyxz"

        }

        if not digits:
            return []

        res = []
        def dp(i, currStr):
            if i >= len(digits):
                res.append(currStr)
                return
            
            #Otherwise we call this fcn with each letter from corresponding digit

            tmp = letDict[digits[i]]

            for letter in tmp:
                dp(i+1, currStr+letter)
        
        dp(0, "")

        return res