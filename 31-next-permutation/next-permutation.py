class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while nums[i-1]>=nums[i] and i>0:
            i-=1
        if i==0:
            nums.reverse()
            return
        j=len(nums)-1
        while nums[i-1]>=nums[j] and j>=i:
            j-=1
        nums[i-1], nums[j]=nums[j], nums[i-1]
        nums[i:]=reversed(nums[i:])
        