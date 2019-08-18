file_name=input("Enter the filename:")
try:
    file_handler=open(file_name)
except:
    print("File",file_name,"does not exist")
    quit()
count = 0
total =0.0
average = 0.0
for line in file_handler:
    if(line.startswith("X-DSPAM-Confidence:") == True):
        pos = line.find(":")
        total = total + float(line[int(pos)+2:])
        count = count +1
average = total/count
print("Average spam confidence:",average)