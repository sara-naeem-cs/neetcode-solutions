class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        r = 0
        window = set()
        max_substring = 0


        while r != len(s):
            # while the right is in our window we gotta update l
            while s[r] in window:
                window.remove(s[l]) #remove char
                l = l + 1 #Update pointer
                # Break out once the window doesn't have any more repeats
            
            window.add(s[r])
            r = r + 1

            max_substring = max(max_substring, r-l)

        return max_substring

        