class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # optimize
        l = 0
        for r in range(1,len(nums)):
            if r % 2 ==0 and nums[r] > 0 :
                l = r
            if r % 2 != 0 and nums[r] < 0:
                nums[l] , nums[r] = nums[r] ,nums[l]
                l+= 1
        return nums





        