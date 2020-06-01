from typing import List

class Solution(object):

    def run(self):
        print(str(self.decompressRLElist([4,2,1,3,3,5])) + ' expected [2,2,2,2,3,5,5,5]')


    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        while nums:
            n = nums.pop(0)
            m = nums.pop(0)
            res += [m for i in range(n)]
        return res


if __name__ == '__main__':
    Solution().run()


