from typing import List
def merge_sort(nums: List) -> List:
  # 1. divide list in sub list
  # 2. merge sub list
  if len(nums) == 1:
    return nums
  
  l = merge_sort(nums[:(len(nums)//2)])
  r = merge_sort(nums[(len(nums)//2):])

  res = []
  l_idx, r_idx = 0, 0
  # merge sorted list
  while l_idx <= len(l)-1 and r_idx <= len(r)-1:
    if l[l_idx] < r[r_idx]:
      res.append(l[l_idx])
      l_idx += 1
    else:
      res.append(r[r_idx])
      r_idx += 1

  # append remain
  if l_idx <= len(l)-1:
    res = res + l[l_idx:]
  if r_idx <= len(r)-1:
    res = res + r[r_idx:]
  

  return res