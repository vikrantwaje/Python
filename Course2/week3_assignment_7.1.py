
file_name=input("Enter the name of file:")
try:
	file_handler=open(file_name)
except:
    print("File",file_name,"does not exist")
    quit()
for line in file_handler:
	print((line.upper()).rstrip())