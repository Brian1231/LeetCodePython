class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0;
        for num in nums:
            sum += num

        return (len(nums) * (len(nums) + 1)) / 2 - sum