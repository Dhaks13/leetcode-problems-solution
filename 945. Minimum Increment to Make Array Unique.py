class Solution(object):
    def minIncrementForUnique(self, nums):
        if not nums:
            return 0

        nums.sort()
        moves = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                moves += prev + 1 - nums[i]
                prev += 1
            else:
                prev = nums[i]

        return moves
