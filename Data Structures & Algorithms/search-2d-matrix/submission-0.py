class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        row = -1

        while t <= b:
            mid = (t + b) // 2
            if target > matrix[mid][-1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                row = mid
                break

        if row == -1:
            return False

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            rowMid = (l + r) // 2
            if target > matrix[row][rowMid]:
                l = rowMid + 1
            elif target < matrix[row][rowMid]:
                r = rowMid - 1
            else:
                return True

        return False