class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        not_equal = 0
        clean_s = ""

        for letter in s:
            if letter.isalnum():
                clean_s = clean_s + letter

        clean_s = clean_s.lower()

        r = 0
        l = len(clean_s) - 1

        while r != l and r<l:
            if clean_s[r] != clean_s[l]:
                not_equal = not_equal + 1
            r = r + 1
            l = l - 1
        
        return not_equal <=1


