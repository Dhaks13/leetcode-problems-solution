class Solution(object):
    def mark(self, index, marked):
        if index not in marked:
            marked.add(index)
            marked.add(index - 1)
            marked.add(index + 1)
            return True
        return False

    def findScore(self, nums):
        score = 0
        marked = set()

        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()

        for val, ind in indexed_nums:
            if self.mark(ind, marked):
                score += val

        return score
