def max(a,b,c):
 if (a >= b) and (a >= c):
    largest = a
 elif (b >= a) and (b >= c):
    largest = b
 else:
    largest = c
 return largest
a = 10
b = 12
c = 13
print(max(a,b,c))