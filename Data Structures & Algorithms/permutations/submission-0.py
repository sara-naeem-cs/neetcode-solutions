class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums)==0:
            return [[]] 

        #Keep calling recursive function with nums without first element
        perms = self.permute(nums[1:]) # Gets permutations of sub lists

        #Add number at index zero into each possible position
        res = []
        #Go through all permutations we have
        #For each permutation go through each index we can insert current value into permutation
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy() #Create copy of permutation
                p_copy.insert(i, nums[0]) #insert num at index into the copy
                res.append(p_copy) #append the result to our res




        return res
        

        
        