class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Using hashmap to store the prefix sum count and if there is subarray with the sum the we can cut then increase the count
        prefix_sum_count = {0:1}
        count = 0
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            if (sum1 -k) in prefix_sum_count:
                count += prefix_sum_count[sum1 -k]
            if sum1 in prefix_sum_count:
                prefix_sum_count[sum1] += 1
            else:
                prefix_sum_count[sum1] = 1
        return count

        
