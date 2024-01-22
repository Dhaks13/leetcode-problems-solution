# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def value(self, l):
        sum=l.val
        c=1
        while l.next is not None:
            l=l.next
            sum+= (l.val*(10**c))
            c+=1
            
        return sum
    
    def create(self, num):
        lis = ListNode()
        cur = lis
        while num!=0:
            cur.val= num%10
            num//=10
            if num != 0:
                cur.next = ListNode()
                cur = cur.next
        return lis
        

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1= self.value(l1)
        val2= self.value(l2)
        sum=val1+val2
        res= self.create(sum)

        return res
            
