x = int(input ())
n = int(input ())
p=n%x
row=n//x+p
if n<x: row=n//x+1
g = n%row
seat =n//x-g
print (row, seat)


row = n // x + 1
seat = n % x
if seat == 0: 
    seat += x
    row -= 1
print(row, seat)

