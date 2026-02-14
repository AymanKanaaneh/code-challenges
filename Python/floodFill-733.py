#https://leetcode.com/problems/flood-fill
#Level: Easy
#Time Complexity: O(n*m), n = len(image), m = len(image[0])
#Space Complexity: O(n*m), n = len(image), m = len(image[0])


class Solution:
    def floodFill(self, image, sr, sc, color):

        rows = len(image)
        cols = len(image[0])
        visited = set()

        def dfs(row, col, original_color):
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                image[row][col] != original_color
            ):
                return

            image[row][col] = color

            if (row, col) not in visited:
                visited.add((row, col))

                dfs(row + 1, col, original_color)  # down
                dfs(row - 1, col, original_color)  # up
                dfs(row, col - 1, original_color)  # left
                dfs(row, col + 1, original_color)  # right

        dfs(sr, sc, image[sr][sc])
        return image
