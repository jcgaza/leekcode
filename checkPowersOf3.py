# UNFINISHED

def checkAnswer(s):
  ans = 0
  for i in s:
    if i > 0:
      ans += 3 ** i
  
  return ans

k = 91
powers = [i for i in range(17) if 3 ** i <= k]

level = 1
stack = [-1] * (len(powers) + 1)
candidates = [[], powers.copy()]

while level != 0:
  while len(candidates[level]) > 0:
    print(candidates)
    stack[level] = candidates[level].pop(0)
    
    print(stack)
    print(checkAnswer(stack))
    if checkAnswer(stack) == k:
      print("HERE")
      print(stack)
      # return True
    elif checkAnswer(stack) > k:
      for i in range(level, len(powers)+1):  # Clear all numbers beyond that level
        stack[i] = -1
    else:
      level += 1
      temp = []

      for num in powers:
        if num not in stack and 3 ** num + checkAnswer(stack) <= k:
          temp.append(num)
      
      candidates.append(temp)

  level -= 1
  candidates.pop()