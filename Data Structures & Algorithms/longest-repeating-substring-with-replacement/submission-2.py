class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #k needs to be >= window - max letters

        l = 0 

        temp_hash = {}
        max_window = 0 

        for r in range(len(s)):
            temp_hash[s[r]] =  1 + temp_hash.get(s[r],0)

            #Get most freq letter
            letter = max(temp_hash, key=temp_hash.get) 

            while (r - l + 1) - temp_hash[letter] > k:
                #remove l from temp_hash
                temp_hash[s[l]] = temp_hash[s[l]] - 1

                #update l
                l = l + 1

            #update window size
            max_window = max(max_window, r - l + 1)
                
        return max_window
        