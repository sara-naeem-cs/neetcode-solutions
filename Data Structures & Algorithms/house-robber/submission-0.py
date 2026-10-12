class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        # [rob1, rob2, n, n+1]

        for n in nums:
            # At n we can choose to keep value rob2 or rob1+n
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp

        return rob2
