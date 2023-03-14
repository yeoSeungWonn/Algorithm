t = int(input())

for _ in range (t):
  stk = []
  isVPS = True
  for ch in input():
    if ch == "(":
      stk.append(ch)
    else:
      if stk:
        stk.pop()
      else:
        isVPS = False
        break

  if stk:
    isVPS = False
    
  print('YES' if isVPS else "NO")

    