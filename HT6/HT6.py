a = 0
for a in range (3,101):
  b = a % 3
  c = a % 5
  if c + b == 0:
    print ('foobar')
  elif b == 0:
    print ('foo')
  elif c == 0:
    print ('bar')
  else:
    print (a)
  a += 1
 
    
    