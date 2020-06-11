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

    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 0 or length == 1:
            return True
        max_el = -1000000
        has_el = False
        for i in range(0, length-1):
            if nums[i] > nums[i+1]:
                # second time next is lesser
                if has_el:
                    return False
                # couldn't replace one
                if nums[i] > max_el and nums[i+1] < max_el:
                    return False
                
                has_el = True
            
            if max_el < nums[i]:
               max_el = nums[i]            
            
        return True
        


if __name__ == '__main__':
    Solution().run()