#  House Robber

from typing import List


class Solution:

    def run(self):
        nums = [1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1]
        print(self.rob(nums))

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # define two sums
        # 1. Exlude previos element
        # 2. Iclude previous element
        val1 = nums[0]
        val2 = nums[1]
        max_value = 0
        for i in range(2,len(nums)):
            # Max from
            # Sum without previous and include current
            # Sum with previous
            max_value = max(val1+nums[i], val2)
            # Swap values
            val1 = val2
            val2 = max_value
        return max_value
        


if __name__ == '__main__':
    Solution().run()

