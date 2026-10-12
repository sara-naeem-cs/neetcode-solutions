class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        all_anas = {}

        for word in strs:
            temp = ''.join(sorted(word))

            if temp not in all_anas:
                #Add sorted word as a key with an empty list
                all_anas[temp] = []
            #Add current word to the list
            all_anas[temp].append(word)

        ret_lst = []

        for k,v in all_anas.items():
            ret_lst.append(v)
        
        return ret_lst

        