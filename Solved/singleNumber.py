# Single Number

from typing import List

class Solution(object):

    def run(self):
        print(str(self.singleNumber([7,1,7,1,2,4,2])) + ' expected 4')
        print(str(self.singleNumber([1,1,2,2,5])) + ' expected 5')
        print(str(self.singleNumber([7,6,6,3,3])) + ' expected 3')
        
    def singleNumberSet(self, nums: List[int]) -> int:
        # Set to store element num[i]
        # remove if already in set
        # last i n set is result
        res = set()
        for i in nums:
            if not i in res:
                res.add(i)
            else:
                res.remove(i)
        if res:
            return res.pop()
        return 0

    def singleNumber(self, nums: List[int]) -> int:
        # Use XOR x^x=0 x^0=x x^y=y^x
        ln = len(nums)
        if ln == 0:
            return 0
        res = nums[0]
        for i in range(1,ln):
            res ^= nums[i]
        return res
        
    
if __name__ == '__main__':
    Solution().run()


