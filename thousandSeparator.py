def thousandSeparator(n):
  copy = str(n)[::-1]
  i = 0
  ans = ""

  while i+3 < len(copy):
    print(copy[i:i+3])
    ans +=  copy[i:i+3] + "."
    i += 3
  
  if i < len(copy):
    ans += copy[i:]

  print(ans[::-1])

thousandSeparator(1234)