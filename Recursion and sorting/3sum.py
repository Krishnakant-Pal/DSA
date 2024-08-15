class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i + 1
            right = len(nums) -1
            while left < right:
                sum1 = nums[left] + nums[right] + nums[i]
                if sum1 < 0:
                    left += 1
                elif sum1 > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res

        