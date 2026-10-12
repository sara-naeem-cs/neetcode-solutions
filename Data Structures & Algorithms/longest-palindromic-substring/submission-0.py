class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = "" #Store resultant palindrome
        resLen = 0

        for i in range(len(s)):
            #Start pointers from centre (in odd case)
            l,r = i, i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                #At this point check if it's the longest
                if resLen < (r-l+1):
                    res = s[l:r+1]
                    resLen = len(res)
                l = l-1
                r = r + 1
            
            #Check for even palindrome
            l,r = i, i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):

                #At this point check if it's the longest
                if resLen < (r-l+1):
                    res = s[l:r+1]
                    resLen = len(res)
                l = l-1
                r = r + 1
        return res           