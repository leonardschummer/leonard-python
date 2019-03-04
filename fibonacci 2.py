n = input("input a postive integer: ")
def function(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (function(n-1)+ function(n-2))
x = function(n)
print(x)
