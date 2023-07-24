x = int(input())
n = int(input())
y = 0
d = 0
while y <= n:
  e = x ** y
  d += e
  y += 1
  print(y, e, d)
print(d)
  
