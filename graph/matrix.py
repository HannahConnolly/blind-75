"""
https://leetcode.com/problems/01-matrix/
Notes:
Checks down and left, uses right and up prev calculated answers
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        max_row = len(mat) - 1
        max_col = len(mat[0]) - 1

        def search(mat, row, col, dist_mat):
            print(row, col)
            # check boundaries
            if row < 0 or col < 0 or row > max_row or col > max_col:
                return 99999999999

            if mat[row][col] is 0:
                return 0

            up = 999999999
            left = 999999999
            right = search(mat, row, col + 1, dist_mat)
            down = search(mat, row + 1, col, dist_mat)
            if row > 0:
                up = dist_mat[row - 1][col]
            if col > 0:
                left = dist_mat[row][col - 1]

            print(right, down, up, left)

            return 1 + min(right, down, up, left)

        dist_mat = [[9999999999 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for row_id, _ in enumerate(mat):
            for col_id, num in enumerate(mat[row_id]):
                print(row_id, col_id, "-*- val:", num, dist_mat)
                dist_mat[row_id][col_id] = search(mat, row_id, col_id, dist_mat)

        return dist_mat
