file_path="myfile.txt"
f1=open(file_path,"r")
print("Initial content of",file_path,":")
print(f1.read())
f1=open(file_path,"a")
text_to_append="\nappending new lines"
f1.write(text_to_append)
f1=open(file_path,"r")
print("\nafter appending : ")
print(f1.read())
f1.close()
