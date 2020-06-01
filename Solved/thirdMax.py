from typing import List

class Solution(object):

    def run(self):
        """print(str(self.thirdMax([1,2,3,2,1,5,6])) + ' expected 3')
        print(str(self.thirdMax([1,2,2,2,1,1,2])) + ' expected 2')
        print(str(self.thirdMax([1,2,3])) + ' expected 1')
        print(str(self.thirdMax([1,2,3,4])) + ' expected 2')
        print(str(self.thirdMax([4,2,1,3])) + ' expected 2')"""
        print(str(self.thirdMax([-4,-2,1,3])) + ' expected -2')


    def thirdMax(self, nums: List[int]) -> int:
        listnums = list(set(nums))
        listnums.sort()
        print(listnums)
        l = len(listnums) 
        if l < 3:
            return listnums.pop() 
        return listnums.pop(l-3)


if __name__ == '__main__':
    Solution().run()


