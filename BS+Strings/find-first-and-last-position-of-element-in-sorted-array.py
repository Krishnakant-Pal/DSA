class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:    
        # finding the target first with binary search then computing the starting and ending binary search.
        def binary_search(nums,target,leftbaise):
            start,end = 0 ,len(nums)-1
            target_index = -1
            
            while start <=end:
                mid = start + (end-start)//2
                if nums[mid] < target:
                    start = mid +1
                elif nums[mid] > target:
                    end = mid -1
                else:
                    target_index = mid
                    # for searching start index we will search towards left side,hence moving end before mid 
                    if leftbaise:
                        end = mid-1
                    else:
                        start = mid +1
            return target_index
        
        # Search left for start index and right for end index 
        left = binary_search(nums,target,True)
        right = binary_search(nums,target,False)
        return [left,right]


            

        

