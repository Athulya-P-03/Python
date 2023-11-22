a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
try:
    c=a/b
    print("a/b : ",c)
except:
    print("Division by zero is not possible")
else:
    print("program excecuted successfully")
