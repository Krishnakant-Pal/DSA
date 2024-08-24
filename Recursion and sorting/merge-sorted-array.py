'''
Merge sorted Array

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
- don't use extra array
Approach
- start with the last value of the array and compare nums1 and nums2 valuse insert the gretest value.
- add leftover values of nums2 in the nums1
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m +n -1
        # iterate over in reverse and add the greater value
        while m >0 and n>0:
            if nums1[m-1] >nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last -=1
        # add the left elements of nums2 to nums1
        while n >0:
            nums1[last] = nums2[n-1]
            n ,last = n-1,last-1


