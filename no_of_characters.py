str=input("Enter a string:")
count=0
for i in range(0,len(str)):
    if (str[i]!=" "):
        count=count+1
print("No.of characters in a string:",count)
