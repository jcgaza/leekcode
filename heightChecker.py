def heightChecker(self, heights: List[int]) -> int:
  copy = heights.copy()
  copy.sort()
  ans = 0
  
  for i in range(len(heights)):
      if heights[i] != copy[i]:
          ans += 1
  return ans