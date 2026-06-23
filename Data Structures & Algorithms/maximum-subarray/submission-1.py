class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=nums[0]
        curr=nums[0]
        for i in range(1,n):
            curr=max(nums[i],curr+nums[i])
            ans=max(ans,curr)
        return ans