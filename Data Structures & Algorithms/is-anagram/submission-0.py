class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len not equal, not anagrams
        if (len(s) != len(t)):
            return False

        s_total = 0
        for c in s:
            s_total = s_total + ord(c)
        
        t_total = 0
        for c in t:
            t_total = t_total + ord(c)
        
        return t_total == s_total


        