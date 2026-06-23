class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        tmp=[]
        for i in nums:
            if i!=0:
                tmp.append(i)
        for i in range(len(nums)):
            if i<len(tmp):
                nums[i]=tmp[i]
            else:
                nums[i]=0

        """
        Do not return anything, modify nums in-place instead.
        """
        