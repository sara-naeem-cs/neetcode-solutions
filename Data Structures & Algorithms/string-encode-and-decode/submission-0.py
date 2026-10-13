class Solution:

#Ascii is from 0-255
    def encode(self, strs: List[str]) -> str:
        #For each string we get the length, convert to string, and append to the word followed by .
        ret_str = ""
        for word in strs:
            ret_str = ret_str + str(len(word)) + "." + word

        return ret_str

    def decode(self, s: str) -> List[str]:
        #Now keep reading characters while they're numbers
        #record as string length x
        #Read in the delimiter
        #take the next x characters as the first word
        #Repeat until no more characters in string

        ret_lst = []
        word_len = ""

        for i in range(len(s)):
            if s[i] != ".":
                word_len = word_len + s[i]
            else:
                #We hit our delimiter
                #Convert word_len to a number
                length = int(word_len)
                #Take in the next word_len characters (i + word_len)
                word = s[i+1:i+length]

                #Append to ret_lst
                ret_lst.append(word)

                #Set i to (i + word_len + 1)
                i = i+length+1

                #Reset word length
                word_len = ""

        return ret_lst





