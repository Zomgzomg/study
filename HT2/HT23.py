x = int(input ())
n = int(input ())
if n<x: row=n//x+1
if n>x: row=n//x
seat=n
if n>x : seat=n//row
print (row, seat)