# Surrounded regions
from typing import List
from math import floor, sqrt

class Solution(object):
    def run(self):

        #print(f'{self.numSquares(12)}, expected 3')
        #print(f'{self.numSquares(48)}, expected 3')
        T = [73,74,75,71,69,72,76,73]
        print(self.dailyTemperaturesBrute(T))

    def dailyTemperaturesBrute(self, T: List[int]) -> List[int]:
        if not T:
            return T
        
        ln = len(T)
        if ln == 1:
            return [0]
        # Brute
        # Find greater temperature
        # O(n**2)
        res = [0]*ln
        for i in range(ln-1):
            for j in range(i, ln):
                if T[j] > T[i]:
                    res[i] = j-i
                    break
        return res



if __name__ == '__main__':
    Solution().run()