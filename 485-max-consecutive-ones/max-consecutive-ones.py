class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # c = 0
        # pc=0

        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         c+=1
        #         pc = max(c,pc)
        #     else:
        #         c=0
        # return pc

        return max(map(len, "".join(map(str, nums)).split("0")))


        