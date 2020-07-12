# Merge Sorted Array

from typing import List


class Solution:

    def run(self):

        nums1 = [1,2,13,0,0,0]
        nums2 = [1,3,5]
        self.merge(nums1, 3, nums2, 3)
        print(nums1)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if n == 0:
            return
        if not nums1 or not nums2:
            return
        
        # Merge lists starting from the end
        # Three pointers
        # targert pos
        k = m+n-1
        # nums1 current
        i = m-1
        # nums2 current
        j = n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        # nums2 tail
        while(j >= 0):
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


if __name__ == '__main__':
    Solution().run()

