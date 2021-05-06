# UNFINISHED
def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
  level = 1
  stack = [0] * len(digits) + 1
  candidates = [[], digits.copy()]

  while level != 0:
    while len(candidates[level]) > 0:
      