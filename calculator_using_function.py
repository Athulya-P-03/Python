def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
print("1.add\n2.substract\n3.multiply\n4.divide")
choice=int(input("Enter your choice(1/2/3/4) : "))
if(choice==1):
    print(num1,"+",num2,"=",add(num1,num2))
elif(choice==2):
    print(num1,"-",num2,"=",substract(num1,num2))
elif(choice==3):
    print(num1,"*",num2,"=",multiply(num1,num2))
elif(choice==4):
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid")
