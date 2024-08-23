class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search 
        start,end = 0 , len(nums) -1
        while start <= end:
            mid = start + (end -start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid +1
            elif nums[mid] > target:
                end = mid -1
    
        # if element not found in array then return the place where the element could be inserted
        if nums[mid] > target:
            return mid
        else:
            return mid +1


        