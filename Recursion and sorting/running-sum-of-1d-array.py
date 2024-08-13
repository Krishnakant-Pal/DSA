class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # initialize the list
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums
