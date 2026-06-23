class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result= nums1[:m]+nums2[:n]
        result.sort()
        nums1[:]=result
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        