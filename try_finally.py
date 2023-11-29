try:
    fileptr=open("abc.txt","r")
    try:
        fileptr.write("Hi Iam good")
    finally:
        fileptr.close()
        print("File closed")
except:
    print("Error")
