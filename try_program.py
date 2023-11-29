f=input("Enter the file name:")
try:
    f1=open(f,"r")
except:
    print("No file named",f)
