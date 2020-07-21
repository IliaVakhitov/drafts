# Number of Islands

from typing import List


class Solution:

    def run(self):
        grid = [["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]

        print(self.numIslands(grid))

    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        stack = []
        rows = len(grid)

        if rows > 0:
            columns = len(grid[0])
        else:
            columns = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    islands += 1
                    stack.append([i, j])
                    while stack:
                        r, c = stack.pop()
                        grid[r][c] = '0'
                        if r < rows-1 and grid[r+1][c] == '1':
                            stack.append([r+1, c])
                        if c < columns-1 and grid[r][c+1] == '1':
                            stack.append([r, c+1])
                        if r > 0 and grid[r-1][c] == '1':
                            stack.append([r-1, c])
                        if c > 0 and grid[r][c-1] == '1':
                            stack.append([r, c-1])
        return islands

if __name__ == '__main__':
    Solution().run()
