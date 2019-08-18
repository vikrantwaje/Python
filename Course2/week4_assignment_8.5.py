file_name = input('Enter the name of file: ')
try:
    file_handler = open(file_name)
except:
    print('Error in opening file',file_name)
    quit()
split_list = list()
count =0
for line in file_handler:
    if(line.startswith('From')):
        split_list = (line.split())
        if(len(split_list) == 7):
            print(split_list[1])
            count = count + 1
print('There were',count,'lines in the file with From as the first word')