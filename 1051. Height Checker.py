class Solution(object):
    def heightChecker(self, heights):
        c = 0
        ex = sorted(heights)
        for i in range(len(heights)):
            if(heights[i] != ex[i]):
                c += 1
        return c
