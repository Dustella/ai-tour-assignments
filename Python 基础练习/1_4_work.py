from math import sin


x = float(input("x: "))

if x <= -1:
    y = 1 + sin(x)
elif -1 <= x <= 2:
    y = abs(x + 1)
else:
    y = x**2 + 3


print("y:", y)
