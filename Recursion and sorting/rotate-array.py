class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # revese the entire arr
        k = k % len(nums)

        l , r = 0, len(nums) -1
        while l < r : 
            nums[l],nums[r] = nums[r] , nums[l]
            l,r = l +1 , r -1

        # reverse upto k
        l , r = 0, k-1
        while l < r :
            nums[l],nums[r] = nums[r] , nums[l]
            l,r = l +1 , r - 1

        # reverse k to end
        l , r = k, len(nums) -1
        while l < r :
            nums[l],nums[r] = nums[r] , nums[l]
            l,r = l +1 , r -1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
           element = nums.pop()
           nums.insert(0,element)