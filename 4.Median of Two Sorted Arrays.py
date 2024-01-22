class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        median=0
        if((len(nums1)%2)==0):
            median=float(nums1[(len(nums1)-2)/2]+nums1[len(nums1)/2])/2
        else: 
            median=nums1[len(nums1)/2]
        return median
