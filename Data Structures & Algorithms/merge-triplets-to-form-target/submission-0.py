class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        aFound = False
        bFound = False
        cFound = False

        for triplet in triplets:
            if not (triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]):
                #Check if we have key num in any position:
                if triplet[0] == target[0]:
                    aFound = True
                if triplet[1] == target[1]:
                    bFound = True
                if triplet[2] == target[2]:
                    cFound = True
        
        return aFound and bFound and cFound

        