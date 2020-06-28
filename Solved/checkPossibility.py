# Non-decreasing Array

from typing import List

class Solution:

    def run(self):
        
        nums = [4,2,3,4,5]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [4,2,1]
        print(f'{self.checkPossibility(nums)} - expected False')

        nums = []
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [4]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [-4,1,2,4]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [3,4,2,3]
        print(f'{self.checkPossibility(nums)} - expected False')

        nums = [3,3,2,3]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [3,4,3,3]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [4,4,3,3]
        print(f'{self.checkPossibility(nums)} - expected False')

        nums = [4,1,3,3]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [4,4,1,3,3]
        print(f'{self.checkPossibility(nums)} - expected False')

        nums = [4,1,1,5,5]
        print(f'{self.checkPossibility(nums)} - expected True')

        nums = [4,4,1,1,5,5]
        print(f'{self.checkPossibility(nums)} - expected False')

    def isNonDecreasing(self, nums: List[int]) -> bool:
        ln = len(nums)
        if ln <= 1:
            return True
        
        for i in range(0, ln-1):
            if nums[i] > nums[i+1]:
                return False

        return True

    def checkPossibility(self, nums: List[int]) -> bool:
        # Brute
        # Delete problem element.
        # Check if is non decreasing
        ln = len(nums)
        if ln <= 1:
            return True
        
        for i in range(1, ln):
            if nums[i-1] > nums[i]:
                return self.isNonDecreasing(nums[:i]+nums[i+1:])\
                    or self.isNonDecreasing(nums[:i-1]+nums[i:])

        return True
        


if __name__ == '__main__':
    Solution().run()