def combine(n: int, k: int):
  # Variables for backtracking
  level = 1
  S = [i for i in range(1, n+1)]
  stack = [0] * (k + 1)
  candidates = [[], S.copy()]
  answers = []

  while level != 0:
    while len(candidates[level]) > 0:
      stack[level] = candidates[level].pop(0) # Get current node
      print(stack, candidates)

      if len(set(stack)) == k+1:  # And if all numbers are unique
        answers.append(stack[1:])
        stack[level] = 0
      else:
        level += 1
        temp = []
        for i in candidates[level-1]:   # Get next candidates based on previous level
          if i not in stack:
            temp.append(i)
        
        candidates.append(temp)

    stack[level] = 0
    level -= 1
    candidates.pop()
  
  return answers
