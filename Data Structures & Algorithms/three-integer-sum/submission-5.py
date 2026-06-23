class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        nums.sort() #O(nlogn)
        res=[]
        for i,ele in enumerate(nums):
            if ele>0: #detect the 1st +ve ele in the nums
                break
            if i>0 and ele==nums[i-1]:#current 1st num is same as the prev 1st num
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                tsum=ele+nums[l]+nums[r]
                if tsum>0:
                    r-=1
                elif tsum<0:
                    l+=1
                else:
                    res.append([ele,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1] :
                        l+=1
        return res


