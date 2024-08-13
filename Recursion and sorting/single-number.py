class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using XOR
        res = 0
        for i in range(len(nums)):
            res = nums[i] ^ res
        return res