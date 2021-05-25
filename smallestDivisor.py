import math
def smallestDivisor(nums,threshold):
  m = max(nums)
  low = 1
  high = m
  
  while low < high:
    mid = (low + high) // 2

    temp = [math.ceil(num/mid) for num in nums]
    sum_temp = sum(temp)
    print(low, high, mid, sum_temp)

    if sum_temp <= threshold:
      high = mid
    else:
      low = mid + 1
  
  return low


print(smallestDivisor([2,3,5,7,11], threshold = 11))