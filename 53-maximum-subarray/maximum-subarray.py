class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        maxs=-inf
        for i in range(len(nums)):
            current+=nums[i]
            maxs=max(current,maxs)
            if current<0:
                current=0
        return maxs
        