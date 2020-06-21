# Rotate Array
from typing import List

class Solution:

    def run(self):        
        for k in range(15):
            nums = [1,2,3,4,5,6,7]
            #self.rotateCycle(nums, k)
            print(self.rotateCopy(nums, k) == self.rotateCycle(nums, k))

        #nums = ['1','2','3','4','5','6','7']
        #self.rotateCycle(nums,2)

    def rotateCopy(self, nums: List[int], k: int) -> None:
        # Brute solution
        # replace elements in a copy
        ln = len(nums)
        if ln == 1:
            return
        if k > ln:
            k =  k % ln
        if k == 0:
            return
        arr = nums.copy()
        for i in range(ln):
            if i+k < ln:
                nums[i+k] = arr[i]
            else:
                nums[i+k-ln] = arr[i]     
            
        return nums

    def rotatePop(self, nums: List[int], k: int) -> None:
        # pop and append element k times
        ln = len(nums)
        if ln == 1:
            return
        if k > ln:
            k =  k % ln
        if k == 0:
            return
        left = False
        if k > ln / 2:
            k = ln - k
            left = True
        for i in range(k):
            if left:
                nums.append(nums.pop(0))
            else:
                nums.insert(0, nums.pop())
        #print(nums)
            
        return nums

    def rotateCycle(self, nums: List[int], k: int) -> None:
        # Replace elements in cycles
        # Define new position for curr element
        # as i + k (i+k-len, if i+ k more than len)
        ln = len(nums)
        if ln == 1:
            return
        if k > ln:
            k =  k % ln
        if k == 0:
            return
        changed = 0
        i = 0        
        while changed < ln:            
            ni = i      
            t = nums[i]
            # Do while j != i and changed < ln
            while changed < ln:                  
                j = ni+k if ni+k < ln else ni+k-ln                                
                pt = nums[j]
                nums[j] = t
                t = pt 
                ni = j                
                changed += 1
                if j == i or changed >= ln:
                    break
            i += 1
            if i >= ln:
                break
        #print(nums)
            
        return nums

if __name__ == '__main__':
    Solution().run()