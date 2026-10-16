class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Have two pointers, i and j, for each word.
        # If letters are equal (i+1, j+1)
        # If letter not equal one of the following will apply:
            # Insert: (i, j+1)
            # Delete: (i+1, j)
            # Replace: (i+1, j+1)

        m, n = len(word1), len(word2)

        # dp[i][j] = fewest edits to turn word1[i:] into word2[j:]
        # The table is (m+1) x (n+1) so the "end of string" row/column fit.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Last column: j is at the end of word2, only deletes are left
        for i in range(m + 1):
            dp[i][n] = m - i

        # Last row: i is at the end of word1, only inserts are left
        for j in range(n + 1):
            dp[m][j] = n - j

        # Fill the rest, bottom-right to top-left
        for i in range(len(word1)-1, -1, -1):       # which rows? which direction?
            for j in range(len(word2)-1, -1, -1):   # which columns?
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]          # match: free, which neighbor?
                else:
                    dp[i][j] = 1 + min(
                        dp[i+1][j],                # insert  (right)
                        dp[i][j+1],                # delete  (down)
                        dp[i+1][j+1],                # replace (diagonal)
                    )

        return dp[0][0]                          # which cell holds the answer?

        """
        
        def dist(i, j, res):
            # Both hit the end of their string:
            if i == len(word1) and j == len(word2):
                return res
            #J is smaller so we would need more inserts:
            if i >= len(word1):
                return res + len(word2) - j
            if j >= len(word2):
                return res + len(word1) - i
            
            if word1[i] == word2[j]:
                #Letters match, no cost
                res = dist(i+1, j+1, res)
            else:
                res = min(dist(i, j+1, res+1), dist(i+1, j, res+1), dist(i+1, j+1, res+1))
            return res

        return dist(0, 0, 0)
        """


        