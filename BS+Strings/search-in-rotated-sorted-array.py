class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums) -1
        while start<=end:
            mid = start +(end-start)//2
            if nums[mid] == target:
                return mid
            # check if left half is ascendingly sorted   [4,5,6,1,2,3]
            elif nums[start] <= nums[mid]:
                if nums[start] <=target <nums[mid]:
                    end = mid-1
                else:
                    start = mid +1
            # else righ half is ascendingly sorted
            else:
                if nums[mid] <= target <=nums[end]:
                    start = mid +1
                else:
                    end = mid -1

        return -1



        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search the minimum element in the array
        def binary_min_index(nums):
            n = len(nums) - 1
            if n ==0: return nums[0]
            start, end= 0,n
            while start<=end:
                mid = start + (end-start)//2
                if nums[mid] <nums[end]:
                    end = mid
                else:
                    start = mid +1
            return mid

        def binary_search(start,end,nums,target):
            while start<= end:
                mid = start + (end-start)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid] < target:
                    start = mid +1
                else:
                    end = mid -1
            return -1
        
        n = len(nums)-1
        # find the index of minimum element
        min_index = binary_min_index(nums)
        
        # search the element in both the part of array
        min_to_last = binary_search(min_index,n,nums,target)
        start_to_min = binary_search(0,min_index-1,nums,target)

        return max(min_to_last,start_to_min)