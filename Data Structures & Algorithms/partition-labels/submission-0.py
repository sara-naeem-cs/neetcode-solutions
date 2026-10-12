class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        #Resultant list
        res = []
        #Letters hashmap with last index of each letter
        letterSet = {}

        for i in range(len(s)-1, -1, -1):
            if s[i] not in letterSet:
                letterSet[s[i]] = i
            
            if len(letterSet) == 26:
                break
        
        #Now we iterate through the string
        size = 0
        partitionEnd = 0
        for i in range(len(s)):
            partitionEnd = max(partitionEnd,letterSet[s[i]])
            size = size + 1

            #What makes us break out of partition?
            if letterSet[s[i]] == i and partitionEnd == i:
                res.append(size)
                #After breaking out reset size and partition end
                size = 0
                partitionEnd = 0

        return res

            
        