import sys


class Solution(object):
    def run(self):

        nums = [1, 3, 5, 6]
        target = 5
        print(f'{self.searchInsert(nums, target)} expected 2')

        nums = [1, 2, 3, 4, 5, 10]
        target = 2
        print(f'{self.searchInsert(nums, target)} expected 2')

        nums = [1, 3, 5, 6]
        target = 7
        print(f'{self.searchInsert(nums, target)} expected 4')

        nums = [1, 3, 5, 6]
        target = 0
        print(f'{self.searchInsert(nums, target)} expected 0')

        bign = 518
        nums = [i for i in range(1000)]
        target = bign
        print(f'{self.searchInsert(nums, target)} expected {bign}')

        nums = []
        target = 5
        print(f'{self.searchInsert(nums, target)} expected 0')

        nums = [1]
        target = 2
        print(f'{self.searchInsert(nums, target)} expected 1')

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # edge cases
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums == 1:
            return 0 if target <= nums[0] else 1
        if nums[0] >= target:
            return 0
        if nums[len_nums-1] < target:
            return len_nums
        if nums[len_nums - 1] == target:
            return len_nums - 1

        i = 0
        j = len(nums) - 1
        m = int(j / 2)
        while i < j:
            if nums[m] == target:
                return m
            if target > nums[m]:
                i = m + 1
            else:
                j = m - 1
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            m = int(i + (j - i) / 2)

        if nums[i] > target:
            return i
        if nums[i] < target:
            return i+1

