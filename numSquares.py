# Surrounded regions
from typing import List
from math import floor, sqrt

class Solution(object):
    def run(self):

        #print(f'{self.numSquares(12)}, expected 3')
        #print(f'{self.numSquares(48)}, expected 3')
        
        self.printCombinations(48)

    def printCombinations(self, n: int) -> int:
        # Print all combinations for array[1,x]
        max_x = floor(sqrt(n))
        print(max_x)       
        r = 0
        while max_x > 0:
            k = n
            x = max_x
            r += 1  
            max_x -= 1 
            res = []         
            res.append(x)
            while k > 0:
                k -= x**2
                if k <= 0:
                    break
                x = floor(sqrt(k))
                res.append(x)
            print(res)

    def numSquares(self, n: int) -> int:
        pass



if __name__ == '__main__':
    Solution().run()