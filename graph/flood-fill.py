"""
https://leetcode.com/problems/flood-fill/submissions/
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
