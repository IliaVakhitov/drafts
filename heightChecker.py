# Height Checker
from typing import List

class Solution:

    def run(self):
        """
        Constraints:
            1 <= heights.length <= 100
            1 <= heights[i] <= 100

        Input: heights = [1,2,3,4,5]
        Output: 0
        
        Input: heights = [5,1,2,3,4]
        Output: 5

        Input: heights = [1,1,4,2,1,3]
        Output: 3
        """
        nums = [1,1,4,2,1,3]
        print(f'{self.heightChecker(nums)} - expected 3')
        nums = [5,1,2,3,4]
        print(f'{self.heightChecker(nums)} - expected 5')
        nums = [1,2,3,4,5]
        print(f'{self.heightChecker(nums)} - expected 0')

    def heightChecker(self, heights: List[int]) -> int:
        # Brute
        # Make copy, sort, compare elements
        if len(heights) == 1:
            return 0

        arr = heights.copy()
        arr.sort()
        res = len(arr)
        for i in range(len(arr)):
            if arr[i] == heights[i]:
                res -= 1
        return res


if __name__ == '__main__':
    Solution().run()