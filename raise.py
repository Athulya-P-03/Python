try:
    num=int(input("Enter a positive integer :" ))
    if(num<=0):
        raise ValueError("please enter a positive number!")
except ValueError as e:
    print(e)

