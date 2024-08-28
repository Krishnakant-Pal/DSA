# optimized approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0
        twoes = 0
        for i in nums:
            if i == 0:
                zeroes +=1
            elif i == 1:
                ones +=1
            else:
                twoes +=1
        i = 0
        while zeroes or ones or twoes:
            if zeroes > 0:
                nums[i] = 0
                i +=1
                zeroes -=1
            elif ones>0:
                nums[i] = 1
                i +=1
                ones -=1
            else:
                nums[i] = 2
                i +=1
                twoes -=1
                









class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Using Bubble sort
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        