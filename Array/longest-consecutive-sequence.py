class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums
        nums_set = set(nums)
        longest = 0
        # iterate over arr
        for num in nums:
            length = 0
            #check if the number is start of a sequence then
            if (num - 1) not in nums_set:
                # check if the next sequence element exits
                while (num + length) in nums_set:
                    length += 1
            longest = max(length,longest)
        return longest