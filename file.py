print("--------------------Welcome to basic file read and write program------------------")
opt=int(input("Enter 1 for write and 2 for read: "))
def write_file():
    file_name=input("Enter the file name: ")
    file=open(file_name,"w")
    string=input("File has been created ,enter a string to write in file:")
    file.write(string)
    file.close()

def read_file():
    file_name=input("Enter the file name: ")
    file=open(file_name, "r")
    print(file.read())
    print("File has been read")
    for i in file:
        print(i)
    else:
        print("File does not exist")
if opt==1:
    write_file()
elif opt==2:
    read_file()

else:
    print("Invalid option")