n = input("input a positive integer:  ")
def F(n):
    return ((1+(5**0.5))**n-(1-(5**0.5))**n)/(2**n*(5**0.5))
x = F(n)
print(x)
