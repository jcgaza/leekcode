def threeConsecutiveOdds(arr):
  index = 0

  while index+2 < len(arr):
    print(arr[index])
    print(arr[index+1])
    print(arr[index+2])
    if arr[index] % 2 != 0 and arr[index+1] % 2 != 0 and arr[index+2] % 2 != 0:
      return True

    if arr[index+2] % 2 == 0:
      index += 3
      continue
    
    if arr[index+1] % 2 == 0:
      index += 2
      continue
    
    index += 1
  
  return False
