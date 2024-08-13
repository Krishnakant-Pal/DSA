def selection_sort(nums):
    minindex = 0
    for i in range(len(nums )-1):
        minindex = i
        for j in range(i,len(nums)):
            if nums[j]< nums[minindex]:
                minindex = j

        nums[i],nums[minindex] = nums[minindex],nums[i]
    return nums

print(selection_sort([9,8,7,6,5,4,3,2,1]))