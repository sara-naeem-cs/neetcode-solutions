class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #all_anas = {}

        #for word in strs:
        #    temp = ''.join(sorted(word))

        #    if temp not in all_anas:
                #Add sorted word as a key with an empty list
        #        all_anas[temp] = []
            #Add current word to the list
        #    all_anas[temp].append(word)

        #ret_lst = []

        #for k,v in all_anas.items():
        #    ret_lst.append(v)
        
        #return ret_lst */

        all_anas = {}

        for word in strs:
            #Create a freq array for the word
            freq_arr = [0]*26

            for char in word:
                freq_arr[ord(char)-ord('a')] = freq_arr[ord(char)-ord('a')] + 1
            
            freq_arr = tuple(freq_arr)

            if freq_arr not in all_anas:
                #If not in hashmap create an empty list with freq_arr as key
                all_anas[freq_arr] = []

            #Add current word to the list
            all_anas[freq_arr].append(word)

        ret_lst = []
        for k,v in all_anas.items():
            ret_lst.append(v)
        
        return ret_lst
        

        