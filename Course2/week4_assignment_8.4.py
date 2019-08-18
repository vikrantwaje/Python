file_name = input('Enter the file name')
try:
    file_handle = open(file_name)
except:
    print('File',file_name,'not found')
    quit()
word_list=list()
split_list = list()
for line in file_handle:
    split_list = (line).split()
    for words in split_list:
        if((words not in word_list) ):
            word_list.append(words)
word_list.sort()
print(word_list) 