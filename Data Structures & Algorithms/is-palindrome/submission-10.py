class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Convert to lowercase
        s = s.lower()

        cleaned_s = ""

        #Clean out all non alphanumeric characters 
        for letter in s:
            if letter.isalnum():
                cleaned_s = cleaned_s + letter

        s = cleaned_s

        r = 0 
        l = len(s)-1

        while r != l:
            #Check
            print(r)
            if s[r] != s[l]:
                return False

            #Update pointers
            l = l - 1
            r = r + 1
        
        return True
            
        