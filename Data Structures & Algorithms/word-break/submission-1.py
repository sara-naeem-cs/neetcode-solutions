class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        for i in range(len(s), -1, -1):
            dp[i] = False #default is that the word isn't in the string

            #For each letter see if the word starts with word in wordDict
            for word in wordDict:

                #If string starts with the word there are two options
                if s[i:].startswith(word):
                    if len(s[i:]) == len(word): #string and word are the same
                        dp[i] = True
                    else: #String is longer than word, check the substring
                        if len(word) < len(s[i:]) and dp[len(s[i:]) - len(word)]:
                            dp[i] = True
                


        return dp[0]

        

        