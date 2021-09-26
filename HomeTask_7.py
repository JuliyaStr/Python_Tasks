def bank (a, years):

    for i in range (years):
        a = a + (a/100*10)
    return (a)

sum = bank (int(input("Enter number: ")), 
int(input("Years: ")))

print (sum)