class Solution(object):
    def sortColors(self, nums):
        color = [nums.count(0),nums.count(1),nums.count(2)]
        j, i=0, 0
        while(j<3):
            if color[j]>0:
                nums[i] = j
                i += 1
                color[j] -= 1
            if color[j] == 0:
                j += 1
