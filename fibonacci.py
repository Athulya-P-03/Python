def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
num=int(input("Enter a number:"))
if num<=0:
    print("Enter the positive number:")
else:
    print("fibonacci series")
    for i in range(num):
        print(fibonacci(i),end=" ")
