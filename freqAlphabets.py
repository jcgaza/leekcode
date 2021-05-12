def freqAlphabets(s):
  stack = []
  for char in s:
    print(stack)
    if char == "#":
      num1 = stack.pop()
      num2 = stack.pop()
      stack.append(int(num2)*10+int(num1))
    else:
      stack.append(int(char))
  
  return "".join([chr(i+96) for i in stack])
