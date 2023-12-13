file_path = "myfile.txt"
n = 2
file=open(file_path, 'r')
print("First",n,"lines of",file_path,":\n")
for line in range(n):
    print(file.readline().strip())
