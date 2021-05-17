def distributeCandies(self, candyType: List[int]) -> int:
  a = set(candyType)
  ans = len(a)
  
  if ans > (len(candyType)/2):
      return len(candyType)//2
  return ans