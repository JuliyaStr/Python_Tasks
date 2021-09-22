N = int(input('Enter number'))
N = N % (3600*24)
hours = N // 3600
minutes = N % 3600 // 60
seconds = N % 60
print(hours, minutes, seconds)
