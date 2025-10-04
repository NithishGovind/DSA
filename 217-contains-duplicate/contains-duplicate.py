class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
                return True
            else:
                d[nums[i]]=1
        return False
            