N = int(input("Enter the number:\n"))
a = 0
while(N > 0):
    b = N % 10
    a= a + b
    N = N//10
print("Sum:", a)
