class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 #Number of palindromes


        for i in range(len(s)):
            #Start pointers from centre (in odd case)
            l,r = i, i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                #At this point check if it's the longest
                l = l-1
                r = r + 1
                res = res + 1
            
            #Check for even palindrome
            l,r = i, i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                res = res + 1
                l = l-1
                r = r + 1
        return res      