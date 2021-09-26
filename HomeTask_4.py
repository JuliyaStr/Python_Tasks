import math
print("rectangle, triangle, circle")
figure = input("Enter the figure: ")
 
if figure == 'rectangle':
    print("Enter side-lengths:")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Square:", (a * b))
elif figure == 'triangle':
    print("Enter side-lengths:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    from math import sqrt
    s = sqrt (p * (p - a) * (p - b) * (p - c))
    print("Square:", s)
elif figure == 'circle':
    r = float(input("Enter radius = "))
    from math import pi
    print("Square:", (pi * r ** 2))

else:
    print("Error")


