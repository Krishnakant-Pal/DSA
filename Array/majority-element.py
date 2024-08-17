class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # My 2nd approach

        # sort the array
        nums.sort()
        majority = len(nums)/2
        count = 1
        l = 0
        # iterate throught the array updating count at each element and
        # check if it is greater than majority
        for r in range(1,len(nums)):
            if nums[l] == nums[r]:
                count += 1
            else:
                l = r
                count = 1
            if count > majority:
                return nums[r]
        if len(nums)< 2:
            return nums[0]
         
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # My approach
        # create a hashmap of to save the counts.
        mymap = {}
        for i in nums:
            if i in mymap.keys():
                mymap[i] += 1
            else:
                mymap[i] = 1

        # iterate over the map to find the count over n/2
        majority = int(len(nums)/2)

        for key,value in mymap.items():
            if value > majority:
                return key