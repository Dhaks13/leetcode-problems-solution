class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable ={}
        ind=[]
        for i in s:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        for i in hashtable:
            if hashtable[i]==1:
                ind.append(s.index(i))
        if(ind):
            return min(ind)
        return -1
