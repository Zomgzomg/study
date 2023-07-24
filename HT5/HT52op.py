x = int(input())
n = int(input())
y = 0
d = 0
for y in range (n):
  e = x ** y
  d += e
  print(y, e, d)
print(d)