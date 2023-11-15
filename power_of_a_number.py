def power(n,p):
    if p<=0:
        return 1
    else:
        return n*power(n,p-1)
a=int(input("Enter a number : "))
b=int(input("Enter a power : "))
power(a,b)
print("power of value is",power(a,b))
    
