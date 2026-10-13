class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #We can create a window of size len(s1)

        if len(s2) < len(s1):
            return False

        #we only have lowercase letters (so 26 letters)


        count_s1 = [0]*26
        #Add letters and counts to this array:
        for letter in s1:
            #we need the ord()-97 of the value
            count_s1[ord(letter)-97] += 1 

        count_tmp = [0] *26     

        window = [] 
        i = 0
        while i <= (len(s2)-len(s1)):
            if i <= len(s1):
                window.append(s2[i])
                count_tmp[ord(s2[i])-97] += 1
            else:
                #window too big, so remove last letter
                element_removed = window.pop(0)
                #Update array to remove last letter
                count_tmp[ord(element_removed)-97] -= 1
                #Add current letter
                window.append(s2[i])
                #Update array with current letter
                count_tmp[ord(s2[i])-97] += 1

            #Check for permutation
            print(count_s1)
            print(count_tmp)
            print("******")
            if count_s1 == count_tmp:
                return True

            
            i = i + 1
        
        return False