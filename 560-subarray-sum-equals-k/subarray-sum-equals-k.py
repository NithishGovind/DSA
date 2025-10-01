class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums=0
        c=0
        d={0:1}
        for i in range(len(nums)):
            sums+=nums[i]
            if (sums-k) in d:
                c +=d[sums-k]
            if sums in d:
                d[sums]+=1
            else:
                d[sums]=1
        return c 

            