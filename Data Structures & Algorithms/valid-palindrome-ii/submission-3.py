class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        clean_s = ""

        for letter in s:
            if letter.isalnum():
                clean_s = clean_s + letter

        clean_s = clean_s.lower()

        r = 0
        l = len(clean_s) - 1


        while r != l and r<l:
            if clean_s[r] != clean_s[l]:
                # See if updating r will give a match:
                if clean_s[r+1] == clean_s[l]:
                    r = r + 1 

                # See if updating l will give a match    
                elif clean_s[r] == clean_s[l-1]:
                    l = l - 1

                else:
                    return False
            else:
                r = r + 1
                l = l - 1

        
        return True


