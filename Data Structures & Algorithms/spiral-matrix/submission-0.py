class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        res = []

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top = top + 1

            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right = right - 1

            if not (left < right and top < bottom):
                break
            
            #Right to left in reverse order
            for i in range(right - 1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom = bottom - 1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left]) #Column fixed, row changes
            
            left = left + 1
        
        return res



        