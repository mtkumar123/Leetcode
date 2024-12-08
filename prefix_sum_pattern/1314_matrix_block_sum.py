""" 
[
[        ]
[        ]
[ , 1,2,3],
[ , 4,5,6],
[ , 7,8,9]
]
[12,21,16],
[27,45,33],
[24,39,28]
"""

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        # zero padding top and left
        sum_matrix = [[0 for i in range(c + 1)] for j in range(r + 1)]
        # First let's create the sum matrix
        # here the bottom right element will hold the sum
        # of all the elements to the left and above
        for rindex, row in enumerate(mat):
            sum = 0
            for cindex, col in enumerate(row):
                sum += col
                sum_matrix[rindex + 1][cindex + 1] = (
                    sum + sum_matrix[rindex][cindex + 1]
                )

        # sum matrix has been formed
        # now form the result matrix
        ans = [[0 for i in range(c)] for j in range(r)]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                b_right_r = min(i + k, r)
                b_right_c = min(j + k, c)

                above_row = max(i - k - 1, 0)
                left_col = max(j - k - 1, 0)

                readd_row, readd_col = above_row, left_col

                sum = (
                    sum_matrix[b_right_r][b_right_c]
                    - sum_matrix[above_row][b_right_c]
                    - sum_matrix[b_right_r][left_col]
                    + sum_matrix[readd_row][readd_col]
                )
                ans[i - 1][j - 1] = sum
        return ans


if __name__ == "__main__":
    s = Solution()
    s.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
