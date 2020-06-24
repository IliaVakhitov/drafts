# Third Maximum Number

from typing import List

class Solution(object):

    def run(self):
        print(str(self.thirdMax([1,3,2,2])) + ' expected 1')
        print(str(self.thirdMax([3,2,2])) + ' expected 3')
        print(str(self.thirdMax([1,2,3,2,1,5,6])) + ' expected 3')
        print(str(self.thirdMax([1,2,2,2,1,1,2])) + ' expected 2')
        print(str(self.thirdMax([1,2,3])) + ' expected 1')
        print(str(self.thirdMax([3,2,1])) + ' expected 1')        
        print(str(self.thirdMax([2,2,2])) + ' expected 2')
        print(str(self.thirdMax([2])) + ' expected 2')
        print(str(self.thirdMax([1,2,3,4])) + ' expected 2')
        print(str(self.thirdMax([4,2,1,3])) + ' expected 2')
        print(str(self.thirdMax([-4,-2,1,3])) + ' expected -2')

    
    def thirdMaxBrute(self, nums: List[int]) -> int:
        # Set and build-in functions
        listnums = list(set(nums))
        listnums.sort()
        print(listnums)
        l = len(listnums) 
        if l < 3:
            return listnums.pop() 
        return listnums.pop(l-3)

    def thirdMax(self, nums: List[int]) -> int:
        # Find 3 max in array in one traverse
        max1 = -float("inf")
        max2 = max1
        max3 = max1
        for i in range(len(nums)):
            if nums[i] > max1:
                max3, max2, max1 = max2, max1, nums[i]
            elif max1 > nums[i] > max2:
                max3, max2 = max2, nums[i]
            elif max2 > nums[i] > max3:
                max3 = nums[i]
            
        return max3 if max2 > max3 > -float("inf") else max1


if __name__ == '__main__':
    Solution().run()


