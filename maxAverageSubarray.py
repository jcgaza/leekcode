def findMaxAverage(nums, k):
  ksum = sum(nums[:k])
  maxAve = ksum / k
  for i in range(k, len(nums)):
      ksum = ksum - nums[i-k] + nums[i]
      if ksum / k > maxAve:
          maxAve = ksum / k
          
  return maxAve

print(findMaxAverage(nums = [0,1,1,3,3], k = 4))