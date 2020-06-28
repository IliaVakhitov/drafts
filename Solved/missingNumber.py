# Missing Number

from typing import List

class Solution:

    def run(self):
        
        nums = [0,2,1]
        print(f'{self.missingNumber(nums)} - expected 0')


    def missingNumber(self, nums: List[int]) -> int:
        # Sum of [1,n] = n*(n+1)/2
        # x+S = n*(n+1)/2, S is sum of array
        # x = Sum - S
        
        # Find sum of array
        
        sum_ar = 0
        for i in nums:
            sum_ar += i
        n = len(nums)
        res = int(n*(n+1)/2 - sum_ar)
        return res
        


if __name__ == '__main__':
    Solution().run()