class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        #Take the length of the shorter word to iterate. 
        length = max(len(word1), len(word2))
        ret_str = ""

        for i in range(length):
            if i < len(word1):
                ret_str = ret_str + word1[i]
            if i < len(word2):
                ret_str = ret_str + word2[i]
        
        return ret_str

