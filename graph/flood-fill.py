"""
https://leetcode.com/problems/flood-fill/submissions/

Notes:
Large if statement at beginning of inner function makes it easy for boundaries 

Similar to recursive functions

inner functions do not need self
"""


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        height, width = len(image), len(image[0])

        def bleed(row, col, original_color):
            if (
                row < 0
                or col < 0
                or row >= height
                or col >= width
                or image[row][col] == color
                or image[row][col] != original_color
            ):
                return

            image[row][col] = color

            bleed(row - 1, col, original_color)
            bleed(row + 1, col, original_color)
            bleed(row, col + 1, original_color)
            bleed(row, col - 1, original_color)

        bleed(sr, sc, original_color=image[sr][sc])

        return image
