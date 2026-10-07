def sum67(nums):
  total = 0
  ignore = False
  
  for num in nums:
    if num == 6:
      ignore = True
    elif not ignore:
      total += num
    elif num == 7 and ignore:
      ignore = False
      
  return total