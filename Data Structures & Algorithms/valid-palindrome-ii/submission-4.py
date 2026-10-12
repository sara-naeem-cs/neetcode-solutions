class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        clean_s = ""

        for letter in s:
            if letter.isalnum():
                clean_s = clean_s + letter

        clean_s = clean_s.lower()

        l = 0
        r = len(clean_s) - 1


        while l<r:
            if clean_s[r] != clean_s[l]:
                # Skip left character and check leftover substring
                skip_l = clean_s[l+1:r+1]

                # Skip right character and check leftover substring
                skip_r = clean_s[l: r]

                #The reversed version of the skipped character should equal the substring
                if skip_l == skip_l[::-1] or skip_r == skip_r[::-1]:
                    return True
                else:
                    return False
            else:
                r = r - 1
                l = l + 1

        
        return True


