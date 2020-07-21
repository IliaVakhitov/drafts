# Create Target Array in the Given Order

from typing import List


class Solution:

    def run(self):
        nums = [1,2,3,1,1]
        index = [0,2,3,1,1]
        print(self.createTargetArray(nums, index))

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        res = []
        for i in range(len(index)):
            res = res[:index[i]] + [nums[i]] + res[index[i]:]    

        return res
        # Brute
        """
        res = []
        for i in range(len(index)):
            res.insert(index[i], nums[i])
        return res
        """


if __name__ == '__main__':
    Solution().run()

