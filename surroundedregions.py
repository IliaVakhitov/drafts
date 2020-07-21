# Surrounded regions

from typing import List


class Solution(object):
    def run(self):
        board = [
            ["O","X","X","O","X"],
            ["X","O","O","X","O"],
            ["X","O","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]
        ]



        
        self.solve(board)
        print(board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Add to stack every 'O' and it's adjacent 'O'
        # Remove from stack add to flip_stack
        # If reach border -> empty flip_stack
        # If not pop from flip_stack and flip into 'X"

        if not board:
            return board
        
        flip_stack = []
        stack = []
        visited = []
        rows = len(board)
        columns = 0
        if rows > 0:
            columns = len(board[0])
        # Moving through inner cells
        for i in range(1,rows-1):
            for j in range(1,columns-1):
                if [i,j] in visited:
                    continue
                if board[i][j] == 'O':
                    stack.append([i, j])
                    flip = True
                    while stack:                        
                        r,c = stack.pop()
                        visited.append([r,c])
                        if r < 0 or c < 0 or r == rows or c == columns:
                            continue
                        if board[r][c] != 'O':
                            continue
                        if r == rows - 1\
                            or c == columns - 1\
                            or r == 0 or c == 0:
                            flip = False
                            break
                        flip_stack.append([r,c])
                        if [r-1,c] not in visited:
                            stack.append([r-1,c])
                        if [r+1,c] not in visited:
                            stack.append([r+1,c])
                        if [r,c-1] not in visited:
                            stack.append([r,c-1])
                        if [r,c+1] not in visited:
                            stack.append([r,c+1])
                    if not flip:
                        flip_stack.clear()
                    while flip_stack:
                        r,c = flip_stack.pop()
                        board[r][c] = 'X'
            

if __name__ == '__main__':
    Solution().run()


if __name__ == '__main__':
    Solution().run()