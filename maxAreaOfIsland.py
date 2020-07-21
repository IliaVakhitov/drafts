# Max Area of Island

from typing import List


class Solution:

    def run(self):
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        
        print(f'{self.maxAreaOfIsland(grid)} - expected 6')
        
        grid = [[0,0,0,0,0,0,0,0]]
        print(f'{self.maxAreaOfIsland(grid)} - expected 0')

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      
        return 0


if __name__ == '__main__':
    Solution().run()