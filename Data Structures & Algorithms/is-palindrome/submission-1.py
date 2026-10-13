class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "" or len(s) == 1:
            return True
        s = s.lower()


        #Establishing my two pointers:
        l = 0
        r = len(s)-1

        for i in range(len(s)//2):
            while not s[l].isalnum():
                l = l + 1
            while not s[r].isalnum():
                r = r - 1

            if r < l:
                break
            if s[l] != s[r]:
                return False
            else:
                l = l + 1
                r = r - 1

        return True


        
        