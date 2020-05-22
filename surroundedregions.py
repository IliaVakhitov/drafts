# Surrounded regions
from typing import List


class Solution(object):
    def run(self):
        board = [['X', 'X', 'X', 'X'],
                 ['X', 'O', 'O', 'X'],
                 ['X', 'X', 'O', 'X'],
                 ['X', 'O', 'X', 'X']]
        self.solve(board)
        print(board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    stack.append({'r': i, 'c': j})
                    while stack:
                        curr_item = stack.pop()
                        r = curr_item['r']
                        c = curr_item['c']
                        grid[r][c] = 0
                        if r < rows - 1 and grid[r + 1][c] == 1:
                            stack.append({'r': r + 1, 'c': c})
                        if c < columns - 1 and grid[r][c + 1] == 1:
                            stack.append({'r': r, 'c': c + 1})
                        if r > 0 and grid[r - 1][c] == 1:
                            stack.append({'r': r - 1, 'c': c})
                        if c > 0 and grid[r][c - 1] == 1:
                            stack.append({'r': r, 'c': c - 1})

