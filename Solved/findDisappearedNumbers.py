# Find All Numbers Disappeared in an Array

from typing import List

class Solution(object):

    def run(self):
        print(str(self.findDisappearedNumbers([1,3,2,2])) + ' expected [4]')
        print(str(self.findDisappearedNumbers([1,3,2,4])) + ' expected []')
        print(str(self.findDisappearedNumbers([1,1,2,2])) + ' expected [3,4]')
        print(str(self.findDisappearedNumbers([1,1,1,1])) + ' expected [2,3,4]')
            
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res = [i for i in range(1,len(nums)+1)]
        for i in range(0,len(nums)):
            res[nums[i]-1] = 0
        
        #1. Accepted, but brute 
        # using set
        """
        res = [i for i in range(1,len(nums)+1)]
        for i in range(0,len(nums)):
            res[nums[i]-1] = 0
        
        res = list(set(res))        
        res.pop(0)
        """
        #2. Not accepted
        #for i in range(len(res)-1,-1,-1):
        #    if res[i] == 0:
        #        res.remove(res[i])

        #3. Accepted
        # Two lists
        """
        if not nums:
            return []
        
        res = [i for i in range(1,len(nums)+1)]
        for i in range(0,len(nums)):
            res[nums[i]-1] = 0
        result = []
        for i in range(len(res)):
            if res[i] != 0:
                result.append(res[i])
        return result
        """
        #4. Set included num[i] as -num[i] for all i < len(nums)
        # Positive nums[i] show i+1, which not in list
        # To result add all positive nums[i]
        for i in range(len(nums)):
            j = nums[i] - 1
            if nums[j] > 0:
                nums[j] = -nums[j]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

if __name__ == '__main__':
    Solution().run()


