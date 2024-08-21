class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Approach: 
        # sort the list to avoid duplicate and skip duplicate while looping
        nums.sort()
        res = []
        n = len(nums)
        #fix two numbers at start and start +1 
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
        # take 2 pointer and go through remaining list to find the sum of 4 
                left, right = j + 1, n - 1
                while left < right:
                    sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum4 == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # check for duplicate elements while moving pointers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum4 < target:
                        left += 1
                    else:
                        right -= 1
        return res




        