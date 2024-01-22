class Solution(object):

    def check(self, temp, c):
        for i in temp:
            if i == c:
                return True
        return False

    def nonrepstr(self, s):
        temp = []
        c = 0
        for i in range(len(s)):
            if self.check(temp, s[i]):
                return c
            else:
                temp.append(s[i])
                c += 1
        return c

    def lengthOfLongestSubstring(self, s):
        count = [0]
        for i in range(len(s)):
            count.append(self.nonrepstr(s[i:]))
        return max(count)
