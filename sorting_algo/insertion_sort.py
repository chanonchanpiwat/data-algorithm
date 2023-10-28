from typing import List
def insertion_sort(nums: List) -> List:
    # 1.) [1 2 3 .. x ] iterate
    # 2.) [1  2 9  ]    for 1..i [sorted list] add new element to sorted list [by swap]
    for i in range(1, len(nums)):
        temp_idx = i
        while temp_idx >= 1 and nums[temp_idx] < nums[temp_idx-1]:
            nums[temp_idx], nums[temp_idx -1] = nums[temp_idx-1], nums[temp_idx]
            temp_idx -= 1
    
    return nums
            