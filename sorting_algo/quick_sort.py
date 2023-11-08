from typing import List
def partition(nums: List, start: int, end: int) -> int:
    ''' 
    1. pivot index [last]
    2. less_than pivot more_than
    3. return pivot index
    '''
    pivot = nums[end]
    less_idx = start - 1
    for i in range(start, end):
         if nums[i] < pivot:
            less_idx += 1
            nums[i], nums[less_idx] = nums[less_idx], nums[i]
    nums[end], nums[less_idx+1] = nums[less_idx+1], nums[end]
    return less_idx + 1

def quick_sort(nums: List, start: int, end:int) -> List:
    ''' 
    1. pivot_idx = partition
    2. left = [0,pivot_idx-1] , right = [pivot_idx+1, len(nums)-1]
    3. quick_sort(left) and quick_sort(right) 
    '''
    if start < end:
        pivot_idx = partition(nums, start, end)
        quick_sort(nums, start, pivot_idx-1)
        quick_sort(nums, pivot_idx+1, end)
    
    return nums