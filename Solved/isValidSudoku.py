# Valid Sudoku

from typing import List

class Solution(object):

     def run(self):

          board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

          """
          board = [
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","."]
          ]
          """
          print(self.isValidSudoku(board))

     def isValidSudoku(self, board: List[List[str]]) -> bool:
          # Brute solution
          # Need to make 3*9 checks of arrays
          # Check valid number while generate array
        
        
          for i in range(9):
               #Row
               print('Row')
               print(board[i])
               if not self.isValidArray(board[i]):
                    return False
               # Column
               array = [board[j][i] for j in range(9)]
               print('Column')
               print(array)
               if not self.isValidArray(array):
                    return False
          # Boxes
          for i in range(1,9,3):
               for j in range(1,9,3):
                    #print(f'i={i} - j={j}')
                    array = []
                    for x in range(i-1,i+2):
                         for y in range(j-1,j+2):
                              array.append(board[x][y])
                    print('Box')
                    print(array)
                    if not self.isValidArray(array):
                         return False

               
          return True
    
     def isValidArray(self, array: List[str]) -> bool:
          # Use len of set
          nums = []
          for n in array:
               if n == '.':
                    continue
               nums.append(int(n))
               
          return len(nums) == len(set(nums))
    
if __name__ == '__main__':
    Solution().run()


    