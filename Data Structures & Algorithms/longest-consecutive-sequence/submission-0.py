class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #First create a set from the list of nums
        #For each number see if it's the start of a sequence
            #If yes start counting
            #If not then go next
        nums_set = set(nums)
        max_seq = 0

        for num in nums:
            temp_seq = 1
            seq_index = num
            if (num-1) not in nums_set:
                #This number is the start of a sequence:
                while seq_index+1 in nums_set:
                    temp_seq = temp_seq + 1
                    seq_index = seq_index + 1 
            max_seq = max(temp_seq, max_seq)
        
        return max_seq


         