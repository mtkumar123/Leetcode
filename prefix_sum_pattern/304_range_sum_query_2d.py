from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        sum_matrix = [[0 for i in range(c+1)] for j in range(r+1)]
        # padding extra left with 0
        # padding top with 0
        # trying to store sum in bottom right for each square
        for row, i in enumerate(matrix):
            prefix_sum = 0
            for col, j in enumerate(i):
                prefix_sum += j
                above = sum_matrix[row][col+1]
                sum_matrix[row + 1][col + 1] = prefix_sum + above
        self.sum_matrix = sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        
        # remove the left and top
        above = self.sum_matrix[r1-1][c2]
        left = self.sum_matrix[r2][c1-1]
        top_left = self.sum_matrix[r1-1][c1-1]
        bottom_right = self.sum_matrix[r2][c2]
        
        return bottom_right - above - left + top_left


if __name__ == "__main__":
    s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(s.sumRegion([5,0,0,0], 3))