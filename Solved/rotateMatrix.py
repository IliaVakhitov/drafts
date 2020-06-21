# Rotate Image

from typing import List

class Solution(object):

    def run(self):
        matrix = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
        print(self.rotate(matrix) == self.rotateTranspose(matrix))
    
    def rotateTranspose(self, matrix: List[List[int]]) -> None:
        # Rotate using transpose matrix
        # 1. Find transpose matrix with antidiagonal
        # 2. Reverse elements in each column

        # 1. Find transpose maitrix
        n = len(matrix)-1
        for i in range(n+1):
            for j in range(n-i-1,-1,-1):
                #print(f'{matrix[i][j]} - {matrix[n-j][n-i]}')
                t = matrix[i][j]
                matrix[i][j] = matrix[n-j][n-i]
                matrix[n-j][n-i] = t
        # 2. Reverse each colunm's elements
        for j in range(n+1):
            i = 0
            k = n
            while i < k:
                t = matrix[i][j]
                matrix[i][j] = matrix[k][j]
                matrix[k][j] = t
                i += 1
                k -= 1


        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        # Rotate cycles from outer to inner
        n = len(matrix)-1
        # Cycle through maitix cycles
        for i in range((n+1)//2):
            # Switch elements of the cycle
            for j in range(i, n-i):
                # make 4 replacesments
                # Top
                t = matrix[i][j]
                # Left -> Top 
                matrix[i][j] = matrix[n-j][i]
                # Botton -> Left
                matrix[n-j][i] = matrix[n-i][n-j]
                # Right -> Botton
                matrix[n-i][n-j] = matrix[j][n-i]
                # Right
                matrix[j][n-i] = t
                
        return matrix


if __name__ == '__main__':
    Solution().run()
