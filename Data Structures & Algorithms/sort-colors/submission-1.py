class Solution:
    def sortColors(self, arr: List[int]) -> None:
        z=arr.count(0)
        o=arr.count(1)
        t=arr.count(2)
        arr[:]=[0]*z+[1]*o+[2]*t
        """
        Do not return anything, modify nums in-place instead.
        """
        