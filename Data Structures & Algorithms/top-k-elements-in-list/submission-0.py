class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        values=[]
        counts=[]
        i=0
        n=len(nums)
        while i<n:
            cnt=1
            while i<n-1 and nums[i]==nums[i+1]:
                cnt+=1
                i+=1
            values.append(nums[i])
            counts.append(cnt)
            i+=1
        result=[]
        for _ in range(k):
            max_frequency=-1
            index=1
            for j in range(len(counts)):
                if counts[j]>max_frequency:
                    max_frequency=counts[j]
                    index=j
            result.append(values[index])
            counts[index]=-1
        return result

        