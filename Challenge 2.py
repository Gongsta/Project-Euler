x = 1
y = 2

evenSum = 2

while x<4000000:
    if y>x:
        x = y + x
        evenSum += x
    else:
        y = x + y
        evenSum += y


print(evenSum)