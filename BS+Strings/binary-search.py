class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize start and end
        start,end = 0,len(nums) -1
        # set up a loop
        while start<=end:
            # calculate a mid
            mid = start + (end -start)//2
            # compare mid element with target
            if target <nums[mid]:
                end = mid -1
            elif target > nums[mid]:
                start = mid +1
            else:
                return mid
        return -1 




# Old solution 

  class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       # Binary search
        if not len(nums):
            return -1
        # Create a low,high and mid variable
        low = 0
        high =  len(nums) -1
       # Set a loop
        while low <= high:  
            mid = (low + high)//2
            mid_num = nums[mid]  
       # check mid equals target
            if mid_num == target:
                return mid

        # if target is less than mid, make mid as new high and calculate mid.
            elif target < mid_num:
                high = mid -1

        # elif target is greater that mid , make mid as new low and calcucate new mid
            elif target > mid_num:
                low = mid + 1 

        return -1

  