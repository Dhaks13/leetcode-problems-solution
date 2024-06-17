import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i,j = 0,int
        (math.sqrt(c))+1
        while (i<=j):
                sum = (i*i)+(j*j)
                if(sum==c):
                    return True
                elif (sum>c):
                    j -= 1
                else:
                    i += 1
        return False
