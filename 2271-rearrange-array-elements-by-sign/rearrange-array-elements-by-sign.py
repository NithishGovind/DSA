class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = [0]*len(nums)
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]>0:
                l[pos]=nums[i]
                pos+=2
            else:
                l[neg]=nums[i]
                neg+=2
        return l