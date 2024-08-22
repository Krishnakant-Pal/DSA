class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #initilizing with max value instead of 0 since it can be negative.
        res = max(nums)

        # intialize with 1 since mulitply with zero will result zero
        cur_min,cur_max = 1,1

        # Iterate ove the nums calculating curent max and min ans saving max in result
        for n in nums:
            # if we encounter 0 then reset to 1, multiple by 0 will result in zero
            if n== 0:
                cur_min,cur_max = 1,1
                continue
            # saving the current max since it will reset by new max value    
            temp = cur_max 
            cur_max = max(n * cur_max, n * cur_min , n)
            cur_min = min(n * temp , n*cur_min , n)
            res = max(res, cur_max,cur_min)
        return res






        