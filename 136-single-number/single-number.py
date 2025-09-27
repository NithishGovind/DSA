class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for i in nums:
        #     if i not in d:
        #         d[i] = 0
        #     d[i]+=1
        # for j,k in d.items():
        #     if k==1:
        #         return j
        xor=0
        for i in nums:
            xor^=i
        return xor
           