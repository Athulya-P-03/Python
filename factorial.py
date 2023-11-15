def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)    
number=int(input("Enter a number : "))
print("The factorial of", number, "is", factorial(number))
