# Two Sum
from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # brute solution
    # submitted first
    """
    for i in range(len(nums)):
        a = nums[i]
        for j in range(i+1, len(nums)):
            b = nums[j]
            if a + b == target:
                return [i, j]
    """
    # We do not seek for a,b such as a+b=target
    # We seek for every a b, such as b = target-a
    # Store in dict every b and it index
    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dict:
            return [dict.get(diff), i]
        dict[nums[i]] = i


