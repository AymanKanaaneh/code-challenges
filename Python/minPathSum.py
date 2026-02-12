#https://leetcode.com/problems/minimum-path-sum
#Level: Medium
#Time Complexity: O(n*m), n = len(grid), m = len(grid[0])
#Space Complexity: O(n*m), n = len(grid), m = len(grid[0])

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rs = len(grid)
        cs = len(grid[0])
        memo = {}

        def dfs(r, c):

            if r >= rs or c >= cs:
                return float('inf')
            if r == (rs -1) and c == (cs - 1):
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            

            memo[(r,c)] = min(dfs(r + 1, c), dfs(r, c + 1)) + grid[r][c]

            return memo[(r,c)]



        return dfs(0, 0)
    

# Not my solution, but it is faster than mine and has better space complexity:
#Time Complexity: O(n*m), n = len(grid), m = len(grid[0])
#Space Complexity: O(1)


# class Solution:
#     def minPathSum(self, grid):
#         rs, cs = len(grid), len(grid[0])

#         for r in range(rs):
#             for c in range(cs):
#                 if r == 0 and c == 0:
#                     continue
#                 elif r == 0:
#                     grid[r][c] += grid[r][c-1]
#                 elif c == 0:
#                     grid[r][c] += grid[r-1][c]
#                 else:
#                     grid[r][c] += min(grid[r-1][c], grid[r][c-1])

#         return grid[-1][-1]


#Old solution with time limit exceeded:

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rs = len(grid)
#         cs = len(grid[0])

#         return self.dfs(grid, rs, cs, 0, 0, False)
        
#     def dfs(self, grid, rs, cs, r, c, bottomRight) -> int:
        
#         if r < 0 or c < 0 or r >= rs or c >= cs:
#             if bottomRight:
#                 return 0
#             else:
#                 return (2**31 - 1)


#         if r == (rs - 1) and c == (cs - 1):
#             bottomRight = True

#         sumPath =  min(self.dfs(grid, rs, cs, r+1, c, bottomRight), self.dfs(grid, rs, cs, r, c+1, bottomRight)) + grid[r][c]

#         return sumPath