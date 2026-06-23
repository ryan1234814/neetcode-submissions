class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=nums[0]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                ans=max(ans,s)
        return ans
        

        