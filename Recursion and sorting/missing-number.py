class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = (len(nums)* (len(nums) +1))//2
        return sum1 - sum(nums)
        
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+ 1):
            if i not in nums:
                return i
        
        