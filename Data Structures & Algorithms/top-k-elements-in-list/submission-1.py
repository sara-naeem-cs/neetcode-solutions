class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequency of each number
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # Step 2: Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Step 3: Collect top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        






        #work through list backwards


