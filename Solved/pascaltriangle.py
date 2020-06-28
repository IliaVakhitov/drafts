# Pascal's Triangle

from typing import List

class Solution:

    def run(self):
        
        res = self.generate(15)
        for row in res:
            print(row)


    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        res.append([1,1])
        for i in range(2,numRows):
            row = []
            # Left
            row.append(1)
            # Center
            for j in range(1,i):
                row.append(res[i-1][j-1]+res[i-1][j])
            # Right
            row.append(1)
            res.append(row)
        return res


if __name__ == '__main__':
    Solution().run()