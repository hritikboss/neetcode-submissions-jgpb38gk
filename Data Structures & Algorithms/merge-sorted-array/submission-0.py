class Solution:
    def merge(self, nums1, m, nums2, n):
 
        arr = nums1[:m] + nums2
 
        arr.sort()
 
        nums1[:] = arr