a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #number 3
new_array = [x for x in a if x<5]
print(new_array)

import math #number 4
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

N = int(input("Enter the number:\n")) #number 5
a = 0
while(N > 0):
    b = N % 10
    a= a + b
    N = N//10
print("Sum:", a)

a=int(input("Enter number 1: ")) #number 6
b=int(input("Enter number 2: "))

 
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
 
print(a)

def bank (a, years): #number 7
    
    for i in range (years):
        a = a + (a/100*10)
    return (a)

sum = bank (int(input("Enter number: ")), 
int(input("Years: ")))

print (sum)