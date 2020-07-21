#  Squares of a Sorted Array

from typing import List


class Solution:

    def run(self):
        nums = [-11,-2,13,25,26,27]
        print(self.sortedSquares(nums))

    def sortedSquares(self, A: List[int]) -> List[int]:
        ln = len(A)
        j = 0
        while j < ln and A[j] < 0:
            j += 1
        
        i = j-1
        res = []
        while 0 <= i and j < ln:
            ai = A[i]**2
            aj = A[j]**2
            if ai < aj:
                res.append(ai)
                i -= 1
            else:
                res.append(aj)
                j += 1
        # tails
        while i >= 0:
            res.append(A[i]**2)
            i -= 1
        while j < ln:
            res.append(A[j]**2)
            j += 1
        return res


if __name__ == '__main__':
    Solution().run()

