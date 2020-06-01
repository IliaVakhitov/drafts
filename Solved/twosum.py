
# 1 hour
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
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

    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dict:
            return [dict.get(diff), i]
        dict[nums[i]] = i


