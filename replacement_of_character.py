str=input("Enter a string:")
k="$"
resultant_Str = str[0]+str[1:].replace(str[0],k)
print("Resultant string after replacing: ", resultant_Str)
