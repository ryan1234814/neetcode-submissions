class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i,j in enumerate(nums):
            if i>0 and j==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                sum=j+nums[left]+nums[right]
                if sum ==0:
                    result.append( [j,nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif sum>0:
                    right-=1
                elif sum<0:
                    left+=1
        return result