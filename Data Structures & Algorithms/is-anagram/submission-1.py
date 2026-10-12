class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len not equal, not anagrams
        if (len(s) != len(t)):
            return False

        s = s.lower()
        t = t.lower()
        s_temp = [0]*26
        t_temp = [0]*26

        for char in s:
            s_temp[ord(char)-ord('a')] = s_temp[ord(char)-ord('a')] + 1

        for char in t:
            t_temp[ord(char)-ord('a')] = t_temp[ord(char)-ord('a')] + 1

        return t_temp == s_temp

        