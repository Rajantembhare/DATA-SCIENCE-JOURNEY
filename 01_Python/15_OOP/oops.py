# Hard Python Code: Longest Increasing Path in a Matrix
# Uses DFS + Memoization (Dynamic Programming)

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def dfs(r, c, prev_val):
            # Out of bounds or not increasing
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev_val:
                return 0

            if memo[r][c] != 0:
                return memo[r][c]

            val = matrix[r][c]
            # Explore 4 directions
            up = dfs(r - 1, c, val)
            down = dfs(r + 1, c, val)
            left = dfs(r, c - 1, val)
            right = dfs(r, c + 1, val)

            memo[r][c] = 1 + max(up, down, left, right)
            return memo[r][c]

        longest_path = 0
        for r in range(rows):
            for c in range(cols):
                longest_path = max(longest_path, dfs(r, c, -float("inf")))

        return longest_path


# Example usage:
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

sol = Solution()
print("Longest Increasing Path:", sol.longestIncreasingPath(matrix))
